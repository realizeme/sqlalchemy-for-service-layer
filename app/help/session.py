from typing import Any

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


from app.config.db import Settings


class SessionMaker:
    conn_str: str

    def __init__(self, setting: Settings = Settings()):
        self.conn_str = setting.to_url()

    def get_session(self):
        # engine = create_engine(self.conn_str, connect_args={"check_same_thread": False})
        # db_engine = create_engine(self.conn_str)
        return Session(self.engine())

    def engine(self):
        return create_engine(self.conn_str, echo=True)
