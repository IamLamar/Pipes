import os
from dotenv import load_dotenv

load_dotenv()

CORS_ALLOW_METHODS = ["DELETE", "GET", "OPTIONS", "PATCH", "POST", "PUT"]

CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "accept-language",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]

CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "").split(",")

# Render URL
render_host = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if render_host:
    CORS_ALLOWED_ORIGINS.append(f"https://{render_host}")

CORS_ALLOW_CREDENTIALS = True

CSRF_TRUSTED_ORIGINS = os.getenv("CSRF_TRUSTED_ORIGINS", "").split(",")
if render_host:
    CSRF_TRUSTED_ORIGINS.append(f"https://{render_host}")
