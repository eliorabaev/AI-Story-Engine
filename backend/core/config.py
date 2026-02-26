from typing import Annotated, List
from pydantic_settings import BaseSettings, NoDecode
from pydantic import field_validator

class Settings(BaseSettings):
    API_PREFIX: str = "/api"
    DEBUG: bool = False
    DATABASE_URL: str
    ALLOWED_ORIGINS: Annotated[List[str], NoDecode] = []
    GEMINI_API_KEY: str
    
    @field_validator("ALLOWED_ORIGINS", mode="before")
    def parse_allowed_origins(cls, v: str | List[str]) -> List[str]:
        if isinstance(v, list):
            return v
        return [origin.strip() for origin in v.split(",")] if v else []
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = True
        
        
settings = Settings()
