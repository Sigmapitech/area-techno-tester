# Security Audit Report

This audit reviews a stack including **React/React Flow (UI), FastAPI (Python backend), OAuth, PostgreSQL/SQLAlchemy (DB), Redis (cache),** and **CapacitorJS (mobile).**
We examine common web risks (XSS, CSRF, SQL injection, etc.) and recommend mitigations for each layer.

## Frontend (React & React Flow)
React's JSX rendering engine escapes content by default (script tags are rendered harmless as strings).  
[stackhawk.com](stackhawk.com)  
This means ordinary JSX is safe from script injection.
However, using `dangerouslySetInnerHTML` or manual DOM APIs reintroduces XSS risk.  
[stackhawk.com](stackhawk.com)  
Always sanitize or avoid inserting raw HTML.
Also audit third-party libraries: for example, React Flow (a graph/flow UI lib) currently has no reported vulnerabilities (Snyk reports zero issues).  
[security.snyk.io](security.snyk.io)  
Still, keep React Flow and all NPM packages up-to-date to avoid supply-chain attacks.

### Key mitigations:

- **Sanitize Inputs:** Never use dangerouslySetInnerHTML on untrusted data.
Escape or purge HTML content on the client.
- **CSP Headers:** Serve a strong Content-Security-Policy to block inline scripts and unauthorized sources.  
[dev.to](dev.to)
- **Dependency Hygiene:** Run tools like `npm audit` and pin library versions.
Avoid eval-like functions.
- **React Flow Usage:** Treat React Flow like any UI code: do not pass user-controlled text into its renderers without sanitization.

## Authentication & OAuth
OAuth2 flows and session handling must be hardened.
**Always include a state parameter in OAuth redirects** - a unique, non-guessable value to correlate requests and mitigate CSRF.  
[auth0.com](auth0.com)  
For mobile/native clients (Capacitor), use PKCE (Proof Key for Code Exchange) so authorization codes can't be stolen by a malicious app.  
[capacitorjs.com](capacitorjs.com)  
Strictly validate redirect URIs (no wildcards) to prevent open-redirects or tokens leaking to rogue endpoints.
Secure cookies with HttpOnly, Secure, and SameSite attributes (e.g.
SameSite=Lax blocks most cross-site use).  
[stackhawk.com](stackhawk.com)  
Prefer storing tokens in secure storage (Android Keystore / iOS Keychain) instead of plain localStorage.  
[developers.google.com](developers.google.com)  
Finally, minimize token scope and lifespan (short-lived access tokens, rotating refresh tokens) to limit exposure if a token is compromised.

### Key mitigations:
- **State Parameter:** Use a strong random `state` in OAuth and verify it on return to prevent CSRF.  
[auth0.com](auth0.com)
- **PKCE:** For mobile apps, always use PKCE to secure the OAuth code exchange.  
[capacitorjs.com](capacitorjs.com)
- **Cookie Security:** Set session cookies to `HttpOnly, SameSite='Lax', Secure` to defend against CSRF/hijacking.  
[stackhawk.com](stackhawk.com)
- **Token Storage:** Store tokens only in OS-provided secure storage (Keychain/Keystore), not in browser-accessible storage.  
[developers.google.com](developers.google.com)
- **HTTPS Everywhere:** Ensure all auth endpoints use TLS.

## API Backend (FastAPI & Secure API Design)
FastAPI encourages secure practices but configuration is key.
**Serve only over HTTPS** (e.g. run Uvicorn with SSL certs) to prevent man-in-the-middle attacks.  
For example, never interpolate user data directly into SQL queries or HTML.
Restrict CORS to known origins and required methods; avoid Access-Control-Allow-Origin: * if credentials are used.
Implement rate-limiting or other throttling to mitigate brute force/DoS.
Use proper error handling (no stack traces to clients) and set security headers (HSTS, X-Frame-Options, etc.).
If the API issues cookies, apply the same cookie security as above.
FastAPI's built-in OAuth2 utilities can manage token authentication, but always verify tokens server-side (signature, expiration, scopes).

### Key mitigations:
- **HTTPS Enforcement:** Configure FastAPI (via Uvicorn/nginx) to use TLS for all endpoints.  
[escape.tech](escape.tech)
- **Input Validation:** Define request schemas (Pydantic) for all routes; FastAPI will reject malformed or extra fields.  
[escape.tech](escape.tech)
- **CORS Policy:** Only allow your trusted frontend origins to call the API.
- **Security Headers:** Include CSP, HSTS, X-Content-Type-Options, etc., in all responses.
- **Error Handling:** Don't leak internal info.
  Return generic error messages.
- **Logging/Auditing:** Log failed auth or suspicious inputs for review.

## Database & ORM (PostgreSQL + SQLAlchemy)
Protect against SQL injection and privilege abuse.
**Always use parameterized queries or ORM methods** - never format SQL strings with user input.
Modern DB adapters (e.g.
psycopg2) and SQLAlchemy's query parameters automatically escape values.  
[realpython.com](realpython.com)  
For example, the unsafe pattern `session.query(Model).filter("foo=%s" % user_input)` is vulnerable, whereas `filter(Model.foo == user_input)` or using `:param` bindings is safe.  
[stackoverflow.com](stackoverflow.com)  
Even when using raw SQL (e.g. text()), bind user values via parameters instead of f-strings.  
[realpython.com](realpython.com)

Use a dedicated database user with least privileges (no superuser).
Restrict the app's role to only needed schemas/tables.
Keep PostgreSQL up-to-date and run it on an internal network (don't expose port 5432 publicly).
Consider using row-level security or built-in auth if multi-tenancy is needed.
Regularly back up the database.

### Key mitigations:
- **Parameterized Queries:** Rely on SQLAlchemy ORM or Core binding to separate code from data.
Do not concatenate SQL fragments.  
[realpython.com](realpython.com)
- **Avoid Raw SQL:** If you must use raw queries, bind parameters (e.g. `:name`) and pass values separately.
Avoid dynamic table/column names from user input.  
[realpython.com](realpython.com)
- **Least Privilege:** The database account used by FastAPI should have only required permissions (no CREATE/ALTER unless needed).
- **Network Security:** Allow DB connections only from the backend server (firewall).
Use SSL for any remote DB access.

## In-Memory Cache (Redis)
Redis is powerful but insecure by default.
**Out of the box, Redis has no authentication and binds to all interfaces.**  
[medium.com](medium.com)  
In production, always enable a strong password or ACL and configure `bind 127.0.0.1` (or specific IP) in `redis.conf`.
Do not expose the Redis port to untrusted networks.
As the official docs warn, Redis should only be in a **trusted environment** or behind an application layer.  
[redis.io](redis.io)  
Disable or rename dangerous commands (e.g.
`FLUSHALL`, `CONFIG`) if not needed.
If using Redis for session storage or caching, don't store plaintext sensitive data - treat it like a key-value store only accessed via your API.

### Key mitigations:
- **Authentication:** Set `requirepass` (Redis<6) or use ACLs (Redis>=6) so a password is needed.
- **Network Binding:** Bind Redis to localhost or internal network and firewall the port.  
[redis.io](redis.io)
- **TLS Encryption:** If Redis traffic traverses a network, enable TLS to prevent snooping.
- **Limit Commands:** Use `rename-command` or ACLs to disable harmful commands in production.

## Mobile App (CapacitorJS)
Capacitor wraps web code in a native container.
`Never embed API keys or secrets in the app binary or JavaScript - attackers can reverse-engineer them.  
[capacitorjs.com](capacitorjs.com)  
Offload secret operations to your backend whenever possible.
For OAuth logins, use PKCE (as noted above) and Android/iOS "universal links" instead of custom schemes to avoid deep-link hijacking.
Use the device's secure storage (Keychain/Keystore) or an encrypted plugin for tokens (do not use plain WebView localStorage).  
[developers.google.com](developers.google.com)  
Require HTTPS for all network requests and consider certificate pinning.
Keep Capacitor and all plugins up to date; remove unneeded plugins to reduce the attack surface.
For Android builds, disable debugging and use code obfuscation (ProGuard/R8) to make static analysis harder.

### Key mitigations:
- **No Secrets in Code:** Do not hardcode secrets or API keys in the app.  
[capacitorjs.com](capacitorjs.com)
- **Secure Token Storage:** Store auth tokens only in encrypted native storage.  
[developers.google.com](developers.google.com)
- **OAuth Deep Links:** Use PKCE and avoid weak custom URL schemes.  
[capacitorjs.com](capacitorjs.com)
- **WebView Security:** Apply a strict CSP to any remote content, and disable allowingUnsafeMixedContent.
- **App Hardening:** Turn off debugging, use obfuscation/minification, and validate input from any plugins.

# Summary of Critical Risks
Across all layers, **the highest-risk issues** are those that allow code or query injection and unauthorized access.
For example, XSS in React could expose user tokens;
SQL injection in the API could corrupt or expose your database;
CSRF in auth flows could hijack user actions;
leaving Redis open could let attackers flush or steal cached data;
and storing OAuth tokens insecurely on the client could lead to account compromise.

Each of the above sections identifies mitigations - in summary:
- **Sanitize and Validate Everything:** Use built-in frameworks (React auto-escaping, FastAPI/Pydantic validation) and parameterized queries.  
[stackhawk.com](stackhawk.com) [realpython.com](realpython.com)
- **Harden Auth Flows:** Use OAuth2 best practices (state, PKCE), secure cookies, HTTPS, and short-lived tokens.  
[auth0.com](auth0.com) [capacitorjs.com](capacitorjs.com)
- **Lock Down Infrastructure:** Require passwords for Redis, restrict DB access, enforce HTTPS, and use firewalls.
  Follow principle of least privilege everywhere.

Implementing these recommendations will mitigate CSRF, XSS, SQLi, and related OWASP Top 10 risks, yielding a robust security posture for the given stack.

**Sources:** Authoritative docs and security guides were used, including FastAPI and Capacitor security guides, Redis documentation, and examples of CSRF/XSS/SQL injection prevention.
Each cited source supports the specific mitigation advice above.
