from unittest.mock import AsyncMock
import pytest
import pytest_asyncio
from app.domain.entities.mp3_file import Mp3File
from app.domain.entities.sample import Sample
from app.domain.entities.youtube_audio import YoutubeAudio
from app.domain.services.create_sample_service.create_sample_service_interface import CreateSampleServiceInterface
from app.domain.usecases.create_sample_from_youtube.create_sample_from_youtube_impl import (
    CreateSampleFromYoutubeUseCase,
)
from app.domain.usecases.get_youtube_video.get_youtube_video_interface import GetYoutubeVideoUseCaseInterface
from app.domain.usecases.video_to_audio_converter.video_to_audio_converter_interface import (
    VideoToAudioConverterUseCaseInterface,
)
from app.domain.usecases.youtube_audio.youtube_audio_impl import YoutubeAudioUseCase
from app.domain.usecases.youtube_audio.youtube_audio_interface import YoutubeAudioUseCaseInterface
from app.domain.utils.response import Response


class CreateSampleServiceStub(CreateSampleServiceInterface):
    async def execute(self, mp3_file: Mp3File, minutes_per_sample: int) -> Response[Sample]:
        return await super().execute(mp3_file, minutes_per_sample)


class TestCreateSampleFromYoutubeUseCase:
    VIDEO_URL = "https://www.youtube.com/watch?v=uVjEcIANv1o"
    minutes_per_sample = 5

    @pytest.fixture
    def youtube_audio(self):
        return YoutubeAudio(
            video_url=self.VIDEO_URL, mp3_file=Mp3File(name="Phill Collins - Against All Odds", path="any_path")
        )

    @pytest_asyncio.fixture
    def mock_get_youtube_video_usecase(self):
        return AsyncMock(spec=GetYoutubeVideoUseCaseInterface)

    @pytest_asyncio.fixture
    def mock_video_to_audio_converter_usecase(self):
        return AsyncMock(spec=VideoToAudioConverterUseCaseInterface)

    @pytest_asyncio.fixture
    def youtube_audio_usecase_stub(self):
        return AsyncMock(spec=YoutubeAudioUseCase)

    @pytest_asyncio.fixture
    def create_sample_service_stub(self):
        return CreateSampleServiceStub()

    @pytest_asyncio.fixture
    def create_sample_from_youtube_usecase(self, youtube_audio_usecase_stub, create_sample_service_stub):
        return CreateSampleFromYoutubeUseCase(youtube_audio_usecase_stub, create_sample_service_stub)

    @pytest.mark.asyncio
    async def test_should_be_able_to_create_a_sample_from_youtube_source(
        self,
        youtube_audio_usecase_stub: YoutubeAudioUseCaseInterface,
        create_sample_service_stub,
        create_sample_from_youtube_usecase: CreateSampleFromYoutubeUseCase,
        youtube_audio,
    ):
        youtube_audio_usecase_stub.execute = AsyncMock(return_value=Response(success=True, body=youtube_audio))

        create_sample_service_stub.execute = AsyncMock(return_value=Response(success=True, body="any_body"))

        response = await create_sample_from_youtube_usecase.execute(self.VIDEO_URL, self.minutes_per_sample)

        assert response.success
        assert response.body == "any_body"

    @pytest.mark.asyncio
    async def test_should_return_response_with_error_when_youtube_audio_fails(
        self,
        youtube_audio_usecase_stub: YoutubeAudioUseCaseInterface,
        create_sample_from_youtube_usecase: CreateSampleFromYoutubeUseCase,
    ):
        youtube_audio_usecase_stub.execute = AsyncMock(return_value=Response(success=False, body="any_error"))

        response = await create_sample_from_youtube_usecase.execute(self.VIDEO_URL, self.minutes_per_sample)

        assert not response.success
        assert response.body == "any_error"

    @pytest.mark.asyncio
    async def test_should_return_response_with_error_when_create_sample_service_fails(
        self,
        youtube_audio_usecase_stub: YoutubeAudioUseCaseInterface,
        create_sample_service_stub,
        create_sample_from_youtube_usecase: CreateSampleFromYoutubeUseCase,
        youtube_audio,
    ):
        youtube_audio_usecase_stub.execute = AsyncMock(return_value=Response(success=True, body=youtube_audio))
        create_sample_service_stub.execute = AsyncMock(return_value=Response(success=False, body="any_sample_error"))

        response = await create_sample_from_youtube_usecase.execute(self.VIDEO_URL, self.minutes_per_sample)

        assert not response.success
        assert response.body == "any_sample_error"
