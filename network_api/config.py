import os
from dotenv import load_dotenv

from pathlib import Path

env_path = Path('.env')
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_NAME: str = "network-api"
    PROJECT_VERSION: str = "1.0.0"

    ORIGINS = [
        "http://localhost:4200",
    ]
    API_PREFIX = "/api/v1/network-api"

    # Environment variables
    OPENAPI_STATUS: str = os.getenv("OPENAPI_STATUS")


settings = Settings()
