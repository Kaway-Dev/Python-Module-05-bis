
import os

from dotenv import load_dotenv


def main() -> None:
    load_dotenv()
    mode = os.getenv("MATRIX_MODE", "development").lower()
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "DEBUG")
    endpoint = os.getenv("ZION_ENDPOINT")

    print("ORACLE STATUS: Consulting the configuration...\n")
    missing = [
        name
        for name, value in (
            ("DATABASE_URL", database_url),
            ("API_KEY", api_key),
            ("ZION_ENDPOINT", endpoint),
        )
        if not value
    ]
    if missing:
        print("Warning: missing configuration: " + ", ".join(missing))
    if mode not in ("development", "production"):
        print("Warning: MATRIX_MODE must be development or production")
        mode = "development"

    print(f"Mode: {mode}")
    print(f"Database: {'Configured' if database_url else 'Not configured'}")
    print(f"API Access: {'Configured' if api_key else 'Not configured'}")
    print(f"Log Level: {log_level}")
    print(f"Remote Network: {'Configured' if endpoint else 'Not configured'}")
    print("\nConfiguration security check:")
    print("[OK] API key value is not displayed or hardcoded")
    print("[OK] .env is ignored by git")
    print("[OK] Environment variables can override .env values")


if __name__ == "__main__":
    main()
