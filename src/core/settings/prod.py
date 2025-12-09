import os
import dj_database_url
import dotenv

dotenv.load_dotenv()

database_url = os.getenv("DATABASE_URL")
if not database_url:
    raise RuntimeError("DATABASE_URL is missing")

DATABASES = {
    "default": dj_database_url.parse(
        database_url,
        conn_max_age=600,
        ssl_require=True,
    )
}

# Security settings for Render
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# Add Render domain to CSRF
render_host = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if render_host:
    CSRF_TRUSTED_ORIGINS = [f"https://{render_host}"]
else:
    CSRF_TRUSTED_ORIGINS = []
