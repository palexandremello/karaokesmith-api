import pytest
from unittest.mock import AsyncMock

import pytest_asyncio
from domain.entities.mp3_file import Mp3File
from domain.entities.sample import Sample
from domain.repositories.sample_repository_interface import SampleRepositoryInterface
from domain.services.sample_saver.sample_saver_interface import SampleSaverInterface
from domain.usecases.save_sample.save_sample_impl import SaveSampleUseCase
from domain.utils.response import Response


class TestSaveSampleUseCase:
    @pytest.fixture
    def sample(self):
        return Sample(
            audio_option=Mp3File(name="any_name", path="any_path"),
            name="any_name",
            content=b"any_bytes",
            path="any_path",
        )

    @pytest_asyncio.fixture
    def repository(self):
        return AsyncMock(spec=SampleRepositoryInterface)

    @pytest_asyncio.fixture
    def sample_saver(self):
        return AsyncMock(spec=SampleSaverInterface)

    @pytest_asyncio.fixture
    def save_sample_usecase(self, repository, sample_saver):
        return SaveSampleUseCase(repository=repository, sample_saver=sample_saver)

    @pytest.mark.asyncio
    async def test_save_when_is_successful(self, save_sample_usecase, repository, sample_saver, sample):
        sample_saver.save_sample.return_value = Response(
            success=True,
            body=sample,
        )
        repository.save.return_value = Response(success=True, body=sample)

        response = await save_sample_usecase.save(sample=sample)

        assert response.success
        assert response.body == sample

        repository.save.assert_called_once_with(sample=sample)
        sample_saver.save_sample.assert_called_once_with(sample=sample)