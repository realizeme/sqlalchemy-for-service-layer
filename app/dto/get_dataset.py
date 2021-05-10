from typing import Optional, List

from pydantic import BaseModel

from app.domain.dataset import Dataset


class GetDatasetRequest(BaseModel):
    pass


class ImageInfo:
    pass


class DatasetInfo(BaseModel):
    id: int
    name: str
    description: Optional[str]

    @staticmethod
    def of(dataset: Dataset):
        return DatasetInfo(
            id=dataset.id,
            name=dataset.name,
            description=dataset.description
        )


class GetDatasetResponse(BaseModel):
    result: List[DatasetInfo]

    @staticmethod
    def of(datasets: List[Dataset]):
        return GetDatasetResponse(
            result=[ DatasetInfo.of(data) for data in datasets ]
        )
