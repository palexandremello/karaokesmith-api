import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from app.domain.entities.audio_media import AudioMedia
from app.domain.entities.mp3_file import Mp3File
from app.domain.entities.video_source import VideoSource
from app.domain.entities.youtube_audio import YoutubeAudio
from app.domain.usecases.get_youtube_video.get_youtube_video_interface import GetYoutubeVideoUseCaseInterface

from app.domain.usecases.video_to_audio_converter.video_to_audio_converter_interface import (
    VideoToAudioConverterUseCaseInterface,
)
from app.domain.usecases.youtube_audio.youtube_audio_impl import YoutubeAudioUseCase
from app.domain.utils.response import Response


class TestYoutubeAudioUseCase:
    @pytest.fixture
    def expected_youtube_audio(self):
        return YoutubeAudio(video_url="any_video_url", mp3_file=Mp3File(name="any_title", path="any_path"))

    @pytest.fixture
    def youtube_video_usecase_throws(self):
        return Response(success=False, body=str(Exception("any_error")))

    @pytest.fixture
    def video_to_audio_converter_usecase_throws(self):
        return Response(success=False, body=str(Exception("any_error")))

    @pytest.fixture
    def mock_youtube_video_usecase(self):
        video_source = VideoSource(title="any_title", thumbnail_url="any_thumbnail", path="any_path")
        return Response(success=True, body=video_source)

    @pytest.fixture
    def mock_video_to_audio_converter_usecase(self):
        audio_media = AudioMedia(path="any_path", audio_format="mp3")
        return Response(success=True, body=audio_media)

    @pytest_asyncio.fixture
    def get_youtube_video_usecase_stub(self) -> GetYoutubeVideoUseCaseInterface:
        return AsyncMock(spec=GetYoutubeVideoUseCaseInterface)

    @pytest_asyncio.fixture
    def video_to_audio_converter_usecase_stub(self) -> VideoToAudioConverterUseCaseInterface:
        return AsyncMock(spec=VideoToAudioConverterUseCaseInterface)

    @pytest.fixture
    def youtube_audio_usecase(
        self, get_youtube_video_usecase_stub, video_to_audio_converter_usecase_stub
    ) -> YoutubeAudioUseCase:
        return YoutubeAudioUseCase(get_youtube_video_usecase_stub, video_to_audio_converter_usecase_stub)

    @pytest.mark.asyncio
    async def test_should_be_able_to_return_response_with_YoutubeAudio_when_excute_is_successful(
        self,
        get_youtube_video_usecase_stub: GetYoutubeVideoUseCaseInterface,
        video_to_audio_converter_usecase_stub: VideoToAudioConverterUseCaseInterface,
        youtube_audio_usecase: YoutubeAudioUseCase,
        mock_youtube_video_usecase: Response[VideoSource],
        mock_video_to_audio_converter_usecase: Response[AudioMedia],
        expected_youtube_audio,
    ):
        get_youtube_video_usecase_stub.get = AsyncMock(return_value=mock_youtube_video_usecase)
        video_to_audio_converter_usecase_stub.convert = AsyncMock(return_value=mock_video_to_audio_converter_usecase)

        response = await youtube_audio_usecase.execute("any_video_url")

        assert response.success
        assert response.body == expected_youtube_audio

    @pytest.mark.asyncio
    async def test_should_be_able_to_return_response_with_error_when_GetYoutubeVideoUseCase_throws(
        self,
        get_youtube_video_usecase_stub: GetYoutubeVideoUseCaseInterface,
        youtube_audio_usecase: YoutubeAudioUseCase,
        youtube_video_usecase_throws,
    ):
        get_youtube_video_usecase_stub.get = AsyncMock(return_value=youtube_video_usecase_throws)
        response = await youtube_audio_usecase.execute("any_video_url")

        assert not response.success
        assert response.body == "any_error"

    @pytest.mark.asyncio
    async def test_should_be_able_to_return_response_with_error_when_VideoToAudioConverterUseCase_throws(
        self,
        get_youtube_video_usecase_stub: GetYoutubeVideoUseCaseInterface,
        video_to_audio_converter_usecase_stub: VideoToAudioConverterUseCaseInterface,
        youtube_audio_usecase: YoutubeAudioUseCase,
        mock_youtube_video_usecase,
        video_to_audio_converter_usecase_throws,
    ):
        get_youtube_video_usecase_stub.get = AsyncMock(return_value=mock_youtube_video_usecase)
        video_to_audio_converter_usecase_stub.convert = AsyncMock(return_value=video_to_audio_converter_usecase_throws)

        response = await youtube_audio_usecase.execute("any_video_url")

        assert not response.success
        assert response.body == "any_error"
