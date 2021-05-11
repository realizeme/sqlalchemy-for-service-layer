import abc
import logging
from typing import Optional

from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

from app.domain.common import Base

logger = logging.getLogger(__name__)


class Dataset(Base):
    __tablename__ = "dataset"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    images = relationship("Image", back_populates="dataset", lazy='dynamic', cascade='all,delete,delete-orphan')

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"<Dataset('id:{self.id}', 'name:{self.name}', 'desc:{self.description}'>"
