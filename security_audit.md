# Security Audit Report

This audit reviews a stack including **React/React Flow (UI), FastAPI (Python backend), OAuth, PostgreSQL/SQLAlchemy (DB), Redis (cache),** and **CapacitorJS (mobile).**
We examine common web risks (XSS, CSRF, SQL injection, etc.) and recommend mitigations for each layer.

## Frontend (React & React Flow)
1. **Safe Rendering by Default**  
   React escapes content in JSX, rendering potentially malicious input (e.g., `<script>`) as harmless text.
   This prevents most injection attacks.  
   [source](https://www.stackhawk.com/blog/react-xss-guide-examples-and-prevention/#:~:text=React%20outputs%20elements%20and%20data,render%20it%20as%20a%20string)

2. **Handling Raw HTML Safely**  
   Avoid `dangerouslySetInnerHTML` or manual DOM APIs with untrusted input.
   If raw HTML is required, sanitize or escape it before rendering.  
   [source](https://www.stackhawk.com/blog/react-xss-guide-examples-and-prevention/#:~:text=All%20HTML%20elements%20contained%20by,docs%20also%20mention%20this%20here)

3. **Content Security Policy (CSP)**  
   Apply a strict CSP to block inline scripts, unsafe eval, and unauthorized external resources, limiting the impact of potential XSS.  
   [source](https://dev.to/ceblakely/web-security-for-developers-cross-site-scripting-xss-1hh9#:~:text=,CSP)

4. **Dependency & Supply Chain Security**  
   Keep React, React Flow, and all npm packages updated.
   Audit dependencies (`npm audit`) and avoid dangerous functions like `eval`.
   Even libraries without known issues (e.g., React Flow) should be treated as potentially risky if given untrusted input.  
   [source](https://security.snyk.io/package/npm/react-flow-renderer#:~:text=Direct%20Vulnerabilities)

## Authentication & OAuth
1. **CSRF Protection with State**  
   Always include and validate a random `state` parameter in OAuth redirects.
   This ensures the response matches the initiating request and prevents CSRF.  
   [source](https://auth0.com/docs/secure/attack-protection/state-parameters#:~:text=CSRF%20attacks)

2. **PKCE for Mobile & Native Apps**  
   Use PKCE (Proof Key for Code Exchange) in mobile/native OAuth flows to protect authorization codes from interception.  
   [source](https://capacitorjs.com/docs/guides/security#:~:text=This%20is%20especially%20important%20for,for%20oAuth2%20in%20Capacitor%20apps)

3. **Redirect URI Validation**  
   Only allow exact, trusted redirect URIs—no wildcards—to prevent open redirects and token leakage.

4. **Session & Token Storage Security**
   * **Cookies (Web):** Set `HttpOnly`, `Secure`, and `SameSite=Lax` (or stricter) to reduce CSRF and hijacking risk.  
     [source](https://www.stackhawk.com/blog/react-csrf-protection-guide-examples-and-how-to-enable-it/#:~:text=match%20at%20L1926%20The%20sameSite%3A,depth)
   * **Mobile/Native:** Store tokens only in secure OS-provided storage (Keychain/Keystore), never in browser-accessible storage.  
     [source](https://developers.google.com/identity/protocols/oauth2/resources/best-practices#:~:text=Handle%20user%20tokens%20securely)

5. **Token Management**  
   Minimize risk by issuing short-lived, narrowly scoped access tokens and rotating refresh tokens to limit exposure if compromised.

## API Backend (FastAPI & Secure API Design)
1. **Transport Security (HTTPS/TLS)**  
   Serve all endpoints over HTTPS (e.g., Uvicorn with TLS or behind Nginx) to prevent man-in-the-middle attacks.  
   [source](https://escape.tech/blog/how-to-secure-fastapi-api/#:~:text=First%20step%3A%20Use%20HTTPS%20for,secure%20communication)

2. **Input Validation**  
   Define request schemas with Pydantic to enforce types, lengths, and formats.
   This rejects malformed data and prevents injection.
   Never interpolate raw user input into SQL, HTML, or commands.  
   [source](https://escape.tech/blog/how-to-secure-fastapi-api/#:~:text=Validate%20and%20sanitize%20user%20input)

3. **CORS & Access Control**  
   Restrict CORS to trusted origins and required methods.
   Avoid `Access-Control-Allow-Origin: *` if credentials are used.

4. **Authentication & Session Security**  
   Validate OAuth2/JWT tokens server-side (signature, expiry, scopes).
  If cookies are issued, set `HttpOnly`, `Secure`, and `SameSite` to prevent CSRF and theft.

5. **Abuse Prevention**  
   Apply rate limiting or throttling (e.g., per-user/IP) to block brute force, credential stuffing, or denial-of-service attempts.

6. **Security Headers**  
   Send headers like HSTS, CSP, X-Content-Type-Options, and X-Frame-Options to reduce attack surface.

7. **Error Handling & Logging**  
   Return generic errors without stack traces.
   Internally, log failed auth, suspicious input, and unusual traffic for monitoring and incident response.

## Database & ORM (PostgreSQL + SQLAlchemy)
1. **Parameterized Queries**  
   Always use SQLAlchemy’s ORM methods or parameterized queries to separate code from data.
   Drivers like psycopg2 automatically escape values, preventing SQL injection.
   Never concatenate user input into SQL strings.  
   [source](https://realpython.com/prevent-python-sql-injection/#:~:text=think%20about%20when%20trying%20to,compose%20a%20query%20with%20parameters)

2. **Safe Query Practices**  
   Prefer ORM expressions (e.g., `filter(Model.foo == user_input)`).
   If raw SQL (`text()`) is required, bind parameters (`:param`) instead of f-strings.
   Never allow user-controlled table or column names.  
   [source](https://stackoverflow.com/questions/6501583/sqlalchemy-sql-injection#:~:text=The%20accepted%20answer%20is%20lazy,you%20are%20open%20to%20attack)

3. **Principle of Least Privilege**  
   Use a dedicated DB account with only the permissions required for the app (no `SUPERUSER`, `CREATE`, or `ALTER` unless necessary).
   Restrict access to relevant schemas/tables only.

4. **Network Security**  
   Run PostgreSQL on a private/internal network and block public access to port `5432`.
   If external access is required, enforce SSL/TLS and firewall rules to limit connections to trusted hosts.

5. **Access Control for Multi-Tenancy** 
   In multi-tenant setups, use PostgreSQL Row-Level Security (RLS) or built-in authentication features to isolate tenants at the database layer.

6. **Maintenance & Backups**  
   Keep PostgreSQL patched and updated.
   Automate regular, tested backups to prevent data loss or corruption.

## In-Memory Cache (Redis)
1. **Authentication & Access Control**  
   Redis has no authentication by default.
   Configure a password (`requirepass` for <6, ACLs for ≥6) to restrict access to authorized clients only.  
   [source](https://medium.com/@rizqimulkisrc/redis-security-preventing-unauthorized-access-and-data-leakage-46278d4f2bb3#:~:text=No%20Authentication%20by%20Default)

2. **Network Isolation**  
   Bind Redis to `127.0.0.1` or a private/internal IP, and firewall port `6379`.
   Never expose Redis directly to the public internet.  
   [source](https://redis.io/docs/latest/operate/oss_and_stack/management/security/#:~:text=In%20this%20case%2C%20the%20web,browsers%20accessing%20the%20web%20application)

3. **Transport Encryption**  
   Enable TLS if Redis traffic must cross untrusted or external networks to protect against sniffing and tampering.

4. **Command Restrictions**  
   Disable or rename high-risk commands (e.g., `FLUSHALL`, `CONFIG`, `DEBUG`) or use ACLs to limit their use in production.

5. **Data Handling Practices**  
   Treat Redis as an ephemeral cache, not a secure database.
   Avoid storing sensitive data in plaintext; restrict session/token data access through the backend only.

## Mobile App (CapacitorJS)
1. **No Hardcoded Secrets**  
   Never embed API keys or secrets in the app—binaries and JavaScript can be reverse-engineered.
   Delegate sensitive operations to the backend.  
   [source](https://capacitorjs.com/docs/guides/security#:~:text=Avoid%20Embedding%20Secrets%20in%20Code)

2. **Secure Token Storage**  
   Store auth tokens only in OS-provided secure storage (iOS Keychain, Android Keystore, or encrypted plugins).
   Avoid WebView `localStorage`/`sessionStorage`.  
   [source](https://developers.google.com/identity/protocols/oauth2/resources/best-practices#:~:text=Handle%20user%20tokens%20securely)

3. **OAuth & Deep Link Security**  
   Use PKCE for OAuth flows.
   Prefer universal links (iOS/Android) over custom URL schemes to prevent deep-link hijacking.  
   [source](https://capacitorjs.com/docs/guides/security#:~:text=This%20is%20especially%20important%20for,for%20oAuth2%20in%20Capacitor%20apps)

4. **Transport Security**  
   Enforce HTTPS for all requests.
   Consider certificate pinning to block MITM attacks.

5. **WebView Security**  
   Apply a strict CSP for any remote content and disable `allowingUnsafeMixedContent` to prevent insecure resource loading.

6. **App Hardening**  
   Disable debugging, enable obfuscation/minification (e.g., ProGuard/R8), validate plugin input, keep Capacitor/plugins updated, and remove unused plugins to reduce attack surface.

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
- **Harden Auth Flows:** Use OAuth2 best practices (state, PKCE), secure cookies, and short-lived tokens.  
[source](https://auth0.com/docs/secure/attack-protection/state-parameters#:~:text=CSRF%20attacks) [source](https://capacitorjs.com/docs/guides/security#:~:text=This%20is%20especially%20important%20for,for%20oAuth2%20in%20Capacitor%20apps)
- **Lock Down Infrastructure:** Require passwords for Redis, restrict DB access.
  Follow principle of least privilege everywhere.

---

Implementing these recommendations will mitigate CSRF, XSS, SQLi, and related OWASP Top 10 risks, yielding a robust security posture for the given stack.

**Sources:** Authoritative docs and security guides were used, including FastAPI and Capacitor security guides, Redis documentation, and examples of CSRF/XSS/SQL injection prevention.
Each cited source supports the specific mitigation advice above.
