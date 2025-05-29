import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    debug: str | None = os.environ.get("DEBUG")
    echo_active: str | None = os.getenv("ECHO_ACTIVE")
    