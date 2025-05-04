from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from dotenv import find_dotenv


class Settings(BaseSettings):

    DATABASE_URL: SecretStr = ...
    APP_NAME: SecretStr = ...

    model_config = SettingsConfigDict(
        env_file=find_dotenv(),
        env_file_encoding="utf-8"
    )

settings = Settings()