from app.repository.dataset_repository import DatasetRepository
from app.help.session import SessionMaker
from app.dto.get_dataset import GetDatasetResponse
from app.domain.dataset import Dataset
from app.domain.image import Image


class DatasetService:
    session_maker : SessionMaker
    repository: DatasetRepository

    def __init__(self, session_maker: SessionMaker = SessionMaker()):
        self.session_maker = session_maker
        self.repository = DatasetRepository()

    async def get_all_datasets(self):
        session = self.session_maker.get_session()
        result = await self.repository.get_all(session)
        return GetDatasetResponse.of(result)

    async def create_dataset(self, dataset: Dataset):
        session = self.session_maker.get_session()
        result = await self.repository.create(session, dataset)
        return result

    async def append_image(self, dataset_id: int, image: Image):
        session = self.session_maker.get_session()
        dataset = await self.repository.get_one(session, dataset_id)
        image.dataset = dataset
        dataset.images.append(image)
        return await self.repository.update(session, dataset)
