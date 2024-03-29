import pytest
import pytest_asyncio
from typing import List
from unittest.mock import AsyncMock
from app.domain.entities.mp3_file import Mp3File
from app.domain.services.create_sample_service.create_sample_service import CreateSampleService
from app.domain.services.create_sample_service.sampler_interface import SamplerInterface


class SamplerStub(SamplerInterface):
    def execute(self, mp3_file: Mp3File, minutes_per_sample: int) -> List[Mp3File]:
        return super().execute(mp3_file, minutes_per_sample)


class TestCreateSampleService:
    list_of_samples = [
        Mp3File("roxette - spend my time part 1", path="any_path1"),
        Mp3File("roxette - spend my time part 2", path="any_path2"),
    ]

    paths = [list_of_samples[0].path, list_of_samples[1].path]

    @pytest_asyncio.fixture
    def sampler_stub(self):
        return SamplerStub()

    @pytest_asyncio.fixture
    def create_sample_service(self, sampler_stub):
        return CreateSampleService(sampler_stub)

    @pytest.mark.asyncio
    async def test_should_be_able_to_create_a_response_with_a_list_of_path_of_sample_with_sampler(
        self, sampler_stub, create_sample_service: CreateSampleService
    ):
        sampler_stub.execute = AsyncMock(return_value=self.list_of_samples)

        sample = await create_sample_service.execute(
            mp3_file=Mp3File("roxette - spend my time", "any_path"), minutes_per_sample=5
        )

        assert sample.success
        assert sample.body[0].path == self.paths[0]

    @pytest.mark.asyncio
    async def test_should_return_a_response_with_erro_when_sampler_throws(
        self, sampler_stub, create_sample_service: CreateSampleService
    ):
        sampler_stub.execute = AsyncMock(side_effect=Exception("Any_error"))

        sample = await create_sample_service.execute(
            mp3_file=Mp3File("roxette - spend my time", "any_path"), minutes_per_sample=5
        )

        assert not sample.success
        assert sample.body == "Any_error"
