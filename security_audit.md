# Security Audit Report

This audit reviews a stack including **React/React Flow (UI), FastAPI (Python backend), OAuth, PostgreSQL/SQLAlchemy (DB), Redis (cache),** and **CapacitorJS (mobile).**
We examine common web risks (XSS, CSRF, SQL injection, etc.) and recommend mitigations for each layer.

## Frontend (React & React Flow)
React's JSX rendering engine escapes content by default (script tags are rendered harmless as strings).  
[source](https://www.stackhawk.com/blog/react-xss-guide-examples-and-prevention/#:~:text=React%20outputs%20elements%20and%20data,render%20it%20as%20a%20string)  
This means ordinary JSX is safe from script injection.
However, using `dangerouslySetInnerHTML` or manual DOM APIs reintroduces XSS risk.  
[source](https://www.stackhawk.com/blog/react-xss-guide-examples-and-prevention/#:~:text=All%20HTML%20elements%20contained%20by,docs%20also%20mention%20this%20here)  
Always sanitize or avoid inserting raw HTML.
Also audit third-party libraries: for example, React Flow (a graph/flow UI lib) currently has no reported vulnerabilities (Snyk reports zero issues).  
[source](https://security.snyk.io/package/npm/react-flow-renderer#:~:text=Direct%20Vulnerabilities)  
Still, keep React Flow and all NPM packages up-to-date to avoid supply-chain attacks.

### Key mitigations:

- **Sanitize Inputs:** Never use dangerouslySetInnerHTML on untrusted data.
Escape or purge HTML content on the client.
- **CSP Headers:** Serve a strong Content-Security-Policy to block inline scripts and unauthorized sources.  
[source](https://dev.to/ceblakely/web-security-for-developers-cross-site-scripting-xss-1hh9#:~:text=,CSP)
- **Dependency Hygiene:** Run tools like `npm audit` and pin library versions.
Avoid eval-like functions.
- **React Flow Usage:** Treat React Flow like any UI code: do not pass user-controlled text into its renderers without sanitization.

## Authentication & OAuth
OAuth2 flows and session handling must be hardened.
**Always include a state parameter in OAuth redirects** - a unique, non-guessable value to correlate requests and mitigate CSRF.  
[source](https://auth0.com/docs/secure/attack-protection/state-parameters#:~:text=CSRF%20attacks)  
For mobile/native clients (Capacitor), use PKCE (Proof Key for Code Exchange) so authorization codes can't be stolen by a malicious app.  
[source](https://capacitorjs.com/docs/guides/security#:~:text=This%20is%20especially%20important%20for,for%20oAuth2%20in%20Capacitor%20apps)  
Strictly validate redirect URIs (no wildcards) to prevent open-redirects or tokens leaking to rogue endpoints.
Secure cookies with HttpOnly, Secure, and SameSite attributes (e.g.
SameSite=Lax blocks most cross-site use).  
[source](https://www.stackhawk.com/blog/react-csrf-protection-guide-examples-and-how-to-enable-it/#:~:text=match%20at%20L1926%20The%20sameSite%3A,depth)  
Prefer storing tokens in secure storage (Android Keystore / iOS Keychain) instead of plain localStorage.  
[source](https://developers.google.com/identity/protocols/oauth2/resources/best-practices#:~:text=Handle%20user%20tokens%20securely)  
Finally, minimize token scope and lifespan (short-lived access tokens, rotating refresh tokens) to limit exposure if a token is compromised.

### Key mitigations:
- **State Parameter:** Use a strong random `state` in OAuth and verify it on return to prevent CSRF.  
[source](https://auth0.com/docs/secure/attack-protection/state-parameters#:~:text=CSRF%20attacks)
- **PKCE:** For mobile apps, always use PKCE to secure the OAuth code exchange.  
[source](https://capacitorjs.com/docs/guides/security#:~:text=This%20is%20especially%20important%20for,for%20oAuth2%20in%20Capacitor%20apps)
- **Cookie Security:** Set session cookies to `HttpOnly, SameSite='Lax', Secure` to defend against CSRF/hijacking.  
[source](https://www.stackhawk.com/blog/react-csrf-protection-guide-examples-and-how-to-enable-it/#:~:text=match%20at%20L1926%20The%20sameSite%3A,depth)
- **Token Storage:** Store tokens only in OS-provided secure storage (Keychain/Keystore), not in browser-accessible storage.  
[source](https://developers.google.com/identity/protocols/oauth2/resources/best-practices#:~:text=Handle%20user%20tokens%20securely)
- **HTTPS Everywhere:** Ensure all auth endpoints use TLS.

## API Backend (FastAPI & Secure API Design)
FastAPI encourages secure practices but configuration is key.
**Serve only over HTTPS** (e.g. run Uvicorn with SSL certs) to prevent man-in-the-middle attacks.  
[source](https://escape.tech/blog/how-to-secure-fastapi-api/#:~:text=First%20step%3A%20Use%20HTTPS%20for,secure%20communication)  
Use Pydantic models to validate and sanitize all input (types, lengths, formats) [source](https://escape.tech/blog/how-to-secure-fastapi-api/#:~:text=Validate%20and%20sanitize%20user%20input) - this prevents injection and broken logic.
For example, never interpolate user data directly into SQL queries or HTML.
Restrict CORS to known origins and required methods; avoid Access-Control-Allow-Origin: * if credentials are used.
Implement rate-limiting or other throttling to mitigate brute force/DoS.
Use proper error handling (no stack traces to clients) and set security headers (HSTS, X-Frame-Options, etc.).
If the API issues cookies, apply the same cookie security as above.
FastAPI's built-in OAuth2 utilities can manage token authentication, but always verify tokens server-side (signature, expiration, scopes).

### Key mitigations:
- **HTTPS Enforcement:** Configure FastAPI (via Uvicorn/nginx) to use TLS for all endpoints.  
[source](https://escape.tech/blog/how-to-secure-fastapi-api/#:~:text=First%20step%3A%20Use%20HTTPS%20for,secure%20communication)
- **Input Validation:** Define request schemas (Pydantic) for all routes; FastAPI will reject malformed or extra fields.  
[source](https://escape.tech/blog/how-to-secure-fastapi-api/#:~:text=Validate%20and%20sanitize%20user%20input)
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
[source](https://realpython.com/prevent-python-sql-injection/#:~:text=think%20about%20when%20trying%20to,compose%20a%20query%20with%20parameters)  
For example, the unsafe pattern `session.query(Model).filter("foo=%s" % user_input)` is vulnerable, whereas `filter(Model.foo == user_input)` or using `:param` bindings is safe.  
[source](https://stackoverflow.com/questions/6501583/sqlalchemy-sql-injection#:~:text=The%20accepted%20answer%20is%20lazy,you%20are%20open%20to%20attack)  
Even when using raw SQL (e.g. text()), bind user values via parameters instead of f-strings.  
[source](https://realpython.com/prevent-python-sql-injection/#:~:text=think%20about%20when%20trying%20to,compose%20a%20query%20with%20parameters)

Use a dedicated database user with least privileges (no superuser).
Restrict the app's role to only needed schemas/tables.
Keep PostgreSQL up-to-date and run it on an internal network (don't expose port 5432 publicly).
Consider using row-level security or built-in auth if multi-tenancy is needed.
Regularly back up the database.

### Key mitigations:
- **Parameterized Queries:** Rely on SQLAlchemy ORM or Core binding to separate code from data.
Do not concatenate SQL fragments.  
[source](https://realpython.com/prevent-python-sql-injection/#:~:text=think%20about%20when%20trying%20to,compose%20a%20query%20with%20parameters)
- **Avoid Raw SQL:** If you must use raw queries, bind parameters (e.g. `:name`) and pass values separately.
Avoid dynamic table/column names from user input.  
[source](https://realpython.com/prevent-python-sql-injection/#:~:text=think%20about%20when%20trying%20to,compose%20a%20query%20with%20parameters)
- **Least Privilege:** The database account used by FastAPI should have only required permissions (no CREATE/ALTER unless needed).
- **Network Security:** Allow DB connections only from the backend server (firewall).
Use SSL for any remote DB access.

## In-Memory Cache (Redis)
Redis is powerful but insecure by default.
**Out of the box, Redis has no authentication and binds to all interfaces.**  
[source](https://medium.com/@rizqimulkisrc/redis-security-preventing-unauthorized-access-and-data-leakage-46278d4f2bb3#:~:text=No%20Authentication%20by%20Default)  
In production, always enable a strong password or ACL and configure `bind 127.0.0.1` (or specific IP) in `redis.conf`.
Do not expose the Redis port to untrusted networks.
As the official docs warn, Redis should only be in a **trusted environment** or behind an application layer.  
[source](https://redis.io/docs/latest/operate/oss_and_stack/management/security/#:~:text=In%20this%20case%2C%20the%20web,browsers%20accessing%20the%20web%20application)  
Disable or rename dangerous commands (e.g.
`FLUSHALL`, `CONFIG`) if not needed.
If using Redis for session storage or caching, don't store plaintext sensitive data - treat it like a key-value store only accessed via your API.

### Key mitigations:
- **Authentication:** Set `requirepass` (Redis<6) or use ACLs (Redis>=6) so a password is needed.
- **Network Binding:** Bind Redis to localhost or internal network and firewall the port.  
[source](https://redis.io/docs/latest/operate/oss_and_stack/management/security/#:~:text=In%20this%20case%2C%20the%20web,browsers%20accessing%20the%20web%20application)
- **TLS Encryption:** If Redis traffic traverses a network, enable TLS to prevent snooping.
- **Limit Commands:** Use `rename-command` or ACLs to disable harmful commands in production.

## Mobile App (CapacitorJS)
Capacitor wraps web code in a native container.
`Never embed API keys or secrets in the app binary or JavaScript - attackers can reverse-engineer them.  
[source](https://capacitorjs.com/docs/guides/security#:~:text=Avoid%20Embedding%20Secrets%20in%20Code)  
Offload secret operations to your backend whenever possible.
For OAuth logins, use PKCE (as noted above) and Android/iOS "universal links" instead of custom schemes to avoid deep-link hijacking.
Use the device's secure storage (Keychain/Keystore) or an encrypted plugin for tokens (do not use plain WebView localStorage).  
[source](https://developers.google.com/identity/protocols/oauth2/resources/best-practices#:~:text=Handle%20user%20tokens%20securely)  
Require HTTPS for all network requests and consider certificate pinning.
Keep Capacitor and all plugins up to date; remove unneeded plugins to reduce the attack surface.
For Android builds, disable debugging and use code obfuscation (ProGuard/R8) to make static analysis harder.

### Key mitigations:
- **No Secrets in Code:** Do not hardcode secrets or API keys in the app.  
[source](https://capacitorjs.com/docs/guides/security#:~:text=Avoid%20Embedding%20Secrets%20in%20Code)
- **Secure Token Storage:** Store auth tokens only in encrypted native storage.  
[source](https://developers.google.com/identity/protocols/oauth2/resources/best-practices#:~:text=Handle%20user%20tokens%20securely)
- **OAuth Deep Links:** Use PKCE and avoid weak custom URL schemes.  
[source](https://capacitorjs.com/docs/guides/security#:~:text=This%20is%20especially%20important%20for,for%20oAuth2%20in%20Capacitor%20apps)
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
[source](https://www.stackhawk.com/blog/react-xss-guide-examples-and-prevention/#:~:text=React%20outputs%20elements%20and%20data,render%20it%20as%20a%20string) [source](https://realpython.com/prevent-python-sql-injection/#:~:text=think%20about%20when%20trying%20to,compose%20a%20query%20with%20parameters)
- **Harden Auth Flows:** Use OAuth2 best practices (state, PKCE), secure cookies, HTTPS, and short-lived tokens.  
[source](https://auth0.com/docs/secure/attack-protection/state-parameters#:~:text=CSRF%20attacks) [source](https://capacitorjs.com/docs/guides/security#:~:text=This%20is%20especially%20important%20for,for%20oAuth2%20in%20Capacitor%20apps)
- **Lock Down Infrastructure:** Require passwords for Redis, restrict DB access, enforce HTTPS, and use firewalls.
  Follow principle of least privilege everywhere.

Implementing these recommendations will mitigate CSRF, XSS, SQLi, and related OWASP Top 10 risks, yielding a robust security posture for the given stack.

**Sources:** Authoritative docs and security guides were used, including FastAPI and Capacitor security guides, Redis documentation, and examples of CSRF/XSS/SQL injection prevention.
Each cited source supports the specific mitigation advice above.
