import os
from pydantic_settings import BaseSettings

basedir = os.path.abspath(os.path.dirname(__file__))

class Settings(BaseSettings):
    SECRET_KEY: str = os.environ.get('SECRET_KEY') or 'a_hard_to_guess_string'
    SQLALCHEMY_DATABASE_URI: str = 'sqlite:///' + os.path.join(basedir, 'fastapi-database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    SESSION_COOKIE_HTTPONLY: bool = True
    SESSION_COOKIE_SAMESITE: str = 'Lax'
    SESSION_COOKIE_SECURE: bool = False
    SESSION_TYPE: str = 'filesystem'
    SESSION_COOKIE_NAME: str = 'your-session-cookie-name'
    REMEMBER_COOKIE_HTTPONLY: bool = True
    REMEMBER_COOKIE_DURATION: int = 86400  # 1 day
    ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"

settings = Settings()
