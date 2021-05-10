from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.config.db import Settings


class SessionMaker:
    conn_str: str

    def __init__(self, setting: Settings = Settings()):
        self.conn_str = setting.to_url()

    def get_session(self):
        engine = create_engine(self.conn_str)
        return Session(engine)

