from unittest.mock import AsyncMock
import pytest
import pytest_asyncio
from domain.entities.mp3_file import Mp3File
from domain.entities.sample import Sample
from domain.entities.youtube_audio import YoutubeAudio
from domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface

from domain.usecases.create_sample_from_mp3.create_sample_from_mp3_interface import CreateSampleFromMp3UseCaseInterface
from domain.usecases.create_sample_from_youtube.create_sample_from_youtube_interface import (
    CreateSampleFromYoutubeUseCaseInterface,
)
from domain.usecases.sample.sample_impl import SampleUseCase
from domain.utils.response import Response


class TestSampleUseCase:
    youtube_audio = YoutubeAudio(video_url="any_url", mp3_file=Mp3File(name="any_artist", path="any_path"))
    sample = Sample(audio_option=youtube_audio)
    sample_with_mp3 = Sample(audio_option=Mp3File(name="any_artist", path="any_path"))

    @pytest_asyncio.fixture
    def create_sample_service_stub(self):
        return AsyncMock(spec=CreateSampleServiceInterface)

    @pytest_asyncio.fixture
    def create_sample_from_mp3_usecase_stub(self):
        return AsyncMock(spec=CreateSampleFromMp3UseCaseInterface)

    @pytest_asyncio.fixture
    def create_sample_from_youtube_usecase_stub(self):
        return AsyncMock(spec=CreateSampleFromYoutubeUseCaseInterface)

    @pytest_asyncio.fixture
    def sample_usecase(self, create_sample_from_mp3_usecase_stub, create_sample_from_youtube_usecase_stub):
        return SampleUseCase(
            create_sample_from_mp3_usecase=create_sample_from_mp3_usecase_stub,
            create_sample_from_youtube_usecase=create_sample_from_youtube_usecase_stub,
        )

    @pytest.mark.asyncio
    async def test_should_be_able_to_create_a_sample_from_youtube_usecase(
        self, sample_usecase: SampleUseCase, create_sample_from_youtube_usecase_stub
    ):
        create_sample_from_youtube_usecase_stub.execute = AsyncMock(
            return_value=Response(success=True, body=self.sample)
        )
        response = await sample_usecase.execute(
            name=None,
            minutes_per_sample=5,
            video_url="ANY_URL",
        )

        assert response.success
        assert response.body == self.sample

    @pytest.mark.asyncio
    async def test_should_be_able_to_create_a_sample_from_mp3_usecase(
        self, sample_usecase: SampleUseCase, create_sample_from_mp3_usecase_stub
    ):
        create_sample_from_mp3_usecase_stub.execute = AsyncMock(
            return_value=Response(success=True, body=self.sample_with_mp3)
        )
        response = await sample_usecase.execute(
            name=None,
            minutes_per_sample=5,
            upload_mp3_file="any_mp3_uploaded",
        )

        assert response.success
        assert response.body == self.sample_with_mp3

    @pytest.mark.asyncio
    async def test_should_return_a_response_with_error_when_create_samples_usecase_throws(
        self, sample_usecase: SampleUseCase, create_sample_from_mp3_usecase_stub
    ):
        create_sample_from_mp3_usecase_stub.execute = AsyncMock(return_value=Response(success=False, body="any_error"))
        response = await sample_usecase.execute(
            name=None,
            minutes_per_sample=5,
            upload_mp3_file="any_mp3_uploaded",
        )

        assert not response.success
        assert response.body == "any_error"
