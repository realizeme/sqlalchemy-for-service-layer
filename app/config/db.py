import os
import typing

from dotenv import load_dotenv
from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    host: str
    port: str
    db: str
    user: str
    password: str
    sql_echo: typing.Optional[bool] = False

    def __init__(self):
        load_dotenv()
        super().__init__()

    def to_url(self):
        print(f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}')
        return f'postgresql+psycopg2://{self.user}:{self.password}@{self.host}:{self.port}/{self.db}'

    class Config:
        env_file = ".env"
        fields = {
            'host': {
                'env': 'POSTGRES_HOST',
            },
            'port': {
                'env': 'POSTGRES_PORT'
            },
            'db': {
                'env': 'POSTGRES_DB'
            },
            'password': {
                'env': 'POSTGRES_PASSWORD'
            },
            'user': {
                'env': 'POSTGRES_USER'
            },
            'sql_echo': {
                'env': 'SQL_ECHO'
            }
        }
settings = Settings()
