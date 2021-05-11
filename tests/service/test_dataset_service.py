import pytest

import contextlib
from sqlalchemy import MetaData

from app.service.dataset_service import DatasetService
from app.help.session import SessionMaker
from app.domain.dataset import Dataset
from app.domain.image import Image


# @pytest.fixture(autouse=True)
# def clean_database():
#     session_maker = SessionMaker()
#     meta = MetaData()
#     engine = session_maker.engine()
    # engine.drop()


@pytest.mark.asyncio
async def test_pass_dataset_get_all():
    # given
    dataset_service = DatasetService(SessionMaker())

    # when
    result = await dataset_service.get_all_datasets()

    assert result is not None


@pytest.mark.asyncio
async def test_pass_create_dataset():
    # given
    dataset = Dataset(name='dataset', description="test-dataset")
    image1 = Image(dataset=dataset, path='image-path-1')
    image2 = Image(dataset=dataset, path='image-path-2')
    dataset.images.append(image1)
    dataset.images.append(image2)

    # when
    dataset_service = DatasetService(SessionMaker())
    result = await dataset_service.create_dataset(dataset)

    # then
    assert result is not None


@pytest.mark.asyncio
async def test_pass_update_dataset():
    # given
    dataset_id = 1
    image1 = Image(dataset=None, path='image-path-3')

    # when
    dataset_service = DatasetService(SessionMaker())
    result = await dataset_service.append_image(dataset_id, image1)

    # then
    assert result is not None


@pytest.mark.asyncio
async def test_pass_get_dataset_detail():
    # given
    dataset_id = 1

    # when
    dataset_service = DatasetService(SessionMaker())
    result = await dataset_service.get_one(dataset_id)

    # then
    assert result is not None
    assert result.images.count() > 0
