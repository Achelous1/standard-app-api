from pydantic import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Standard App API"
    database_host: str
    database_name: str
    database_user: str
    database_password: str

    class Config:
        env_file = ".env"