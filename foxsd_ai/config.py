from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent.parent

APP_NAME = "FoxSD AI"
BRAND = "FoxSD"
ALIAS = "Fox"
CONTACT = "foxsd520@gmail.com"

AI_PROVIDER = os.getenv("AI_PROVIDER", "openai_compatible").strip().lower()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "").strip()
OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1").rstrip("/")
MODEL_NAME = os.getenv("MODEL_NAME", "gpt-4o-mini").strip()
ENABLE_LOCAL_FALLBACK = os.getenv("ENABLE_LOCAL_FALLBACK", "true").strip().lower() in {"1", "true", "yes", "on"}

SECURITY_PROMPT_MODE = os.getenv("SECURITY_PROMPT_MODE", "strict").strip().lower()
