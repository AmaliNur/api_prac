from pydantic_settings import BaseSettings, SettingsConfigDict
import os
from pydantic import Field


class PostgresConfig(BaseSettings):
    host: str
    port: int
    database: str
    userr: str
    password: str

    model_config = SettingsConfigDict(env_file=os.path.join('secure/bdd.env'))

    @property
    def connection_string(self):
        return f"postgresql://{self.userr}:{self.password}@{self.host}:{self.port}/{self.database}"


class Settings(BaseSettings):
    # postgres: PostgresConfig = Field(PostgresConfig())
    path_root: str = Field(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


settings = Settings()

if __name__ == '__main__':
    print(settings.model_dump())
