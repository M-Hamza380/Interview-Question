from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()


class Settings(BaseModel):
    debug: bool = True
    echo_active: bool = False

    class Config:
        env_file = ".env"
    