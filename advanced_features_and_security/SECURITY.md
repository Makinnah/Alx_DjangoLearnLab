# Security Configuration

## HTTPS Enforcement
- `SECURE_SSL_REDIRECT = True` ensures all traffic is served over HTTPS.
- HSTS is configured with `SECURE_HSTS_SECONDS = 31536000` to enforce HTTPS for 1 year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS` and `SECURE_HSTS_PRELOAD` applied for full coverage.

## Secure Cookies
- Session and CSRF cookies (`SESSION_COOKIE_SECURE` and `CSRF_COOKIE_SECURE`) are set to True.

## Security Headers
- `X_FRAME_OPTIONS = 'DENY'` protects against clickjacking.
- `SECURE_CONTENT_TYPE_NOSNIFF` prevents MIME type sniffing.
- `SECURE_BROWSER_XSS_FILTER` enables browser XSS filters.

## Deployment
- Nginx/Apache configured to serve HTTPS and redirect all HTTP requests.
- SSL certificates installed and renewed via Let's Encrypt.
