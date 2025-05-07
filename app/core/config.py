from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel
from dotenv import find_dotenv


class RunConfig(BaseModel):
    host: str = 'localhost'
    port: int = 5541


class DataBaseConfig(BaseModel):
    url: str  = ...


class AuthConfig(BaseModel):
    token: str = ...


class Settings(BaseSettings):

    model_config = SettingsConfigDict(
        case_sensitive=False,
        env_nested_delimiter='__',
        env_file=find_dotenv(),
        env_file_encoding="utf-8"
    )

    run: RunConfig = RunConfig()
    db: DataBaseConfig = ...
    auth: AuthConfig = ...

settings = Settings()