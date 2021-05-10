from sqlalchemy.orm import Session
from sqlalchemy.exc import DBAPIError
from sqlalchemy.orm.exc import NoResultFound

from app.domain.dataset import Dataset


class DatasetRepository:

    async def get_all(self, session: Session):
        try:
            return session.query(Dataset).all()
        except Exception as e:
            return []

    async def create(self, session: Session, dataset: Dataset):
        try:
            session.add(dataset)
            session.commit()
            session.refresh(dataset)
        except DBAPIError as e:
            session.rollback()
            raise
        except Exception as e:
            raise
        return dataset

    async def get_one(self, session: Session, dataset_id: int):
        try:
            return session.query(Dataset).filter(Dataset.id == dataset_id).one()
        except Exception as e:
            return None

    async def update(self, session: Session, dataset: Dataset):
        try:
            session.merge(dataset)
            session.commit()
            return dataset
        except NoResultFound as e:
            raise # Notf(F"Dataset with id:{dataset_id} not found")
        except Exception as e:
            raise

