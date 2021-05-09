import abc
import logging
from typing import Optional

from sqlalchemy import BigInteger, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.domain.common import Base

logger = logging.getLogger(__name__)


class Dataset(Base):
    __tablename__ = "dataset"
    id = Column(BigInteger, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    images = relationship("Image", backref="dataset")

    def __repr__(self):
        return f"<Dataset('id:{self.id}', 'name:{self.name}', 'desc:{self.description}'>"
