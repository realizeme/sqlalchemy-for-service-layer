import abc
import logging
from typing import Optional

from sqlalchemy import BigInteger, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import composite, relationship

from app.domain.common import Base

logger = logging.getLogger(__name__)


class Image(Base):
    __tablename__ = "image"
    id = Column(BigInteger, primary_key=True, index=True)
    path = Column(String)
    dataset_id = Column(Integer, ForeignKey('dataset.id'))
    dataset = relationship("Dataset", back_populates="images")

    def __repr__(self):
        return f"<Image('id:{self.id}', 'path:{self.path}'>"
