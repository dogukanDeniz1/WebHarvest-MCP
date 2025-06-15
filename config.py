from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    crawl4ai_docker_url: str
    log_level: str = "INFO"

    class Config:
        env_file = ".env"

settings = Settings()
