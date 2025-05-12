from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from dotenv import find_dotenv


class RunConfig(BaseModel):
    host: str = "localhost"
    port: int = 5541


class DataBaseConfig(BaseModel):
    url: str = ...


class AuthConfig(BaseModel):
    token: str = ...


class DigisellerConfig(BaseModel):
    base_url: str = "https://api.digiseller.ru"
    headers: dict = {"Content-Type": "application/json", "Accept": "application/json"}
    api_key: str = ...
    seller_id: int = 1170447
    timeout: int = 15
    retries: int = 3
    delay: int = 1


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter="__",
        env_file=find_dotenv(),
        env_file_encoding="utf-8",
    )

    run: RunConfig = RunConfig()
    db: DataBaseConfig = ...
    auth: AuthConfig = ...
    digi: DigisellerConfig = ...


settings = Settings()
