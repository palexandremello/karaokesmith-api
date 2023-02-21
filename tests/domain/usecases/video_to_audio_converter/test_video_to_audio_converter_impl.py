import pytest
from unittest.mock import AsyncMock, Mock

import pytest_asyncio
from domain.entities.audio_media import AudioFormat, AudioMedia
from domain.entities.video_source import VideoSource
from domain.services.video_converter.video_converter_service_interface import VideoConverterServiceInterface
from domain.usecases.video_to_audio_converter.video_to_audio_converter_impl import VideoToAudioConverterUseCase
from domain.utils.response import Response


class TestVideoToAudioConverterUseCase:

    @pytest_asyncio.fixture
    def video_converter_service_stub(self) -> VideoConverterServiceInterface:
        return AsyncMock(spec=VideoConverterServiceInterface)
    

    @pytest_asyncio.fixture
    def video_to_audio_usecase(self, video_converter_service_stub):
        return VideoToAudioConverterUseCase(video_converter_service_stub)
    


    @pytest.mark.asyncio
    async def test_should_return_an_AudioMedia_when_video_converter_is_success(self, video_to_audio_usecase,
                                                                         video_converter_service_stub):
        video = VideoSource(title="Real Estate - Paper Cup", thumbnail_url="any_thumbnail_url", path="any_path")
        audio = AudioMedia(path="any_path", audio_format= AudioFormat.MP3)

        video_converter_service_stub.execute = AsyncMock(return_value=audio)

        response = await video_to_audio_usecase.convert(video)


        assert isinstance(response, Response)
        assert response.success
        assert response.body == audio


    @pytest.mark.asyncio
    async def test_should_return_an_response_with_Exception_when_video_converter_has_failed(self, video_to_audio_usecase,
                                                                                      video_converter_service_stub):
        
        video = VideoSource(title="Real Estate - Paper Cup", thumbnail_url="any_thumbnail_url", path="any_path")
        error_message = "Error during audio conversion"
        error = Exception(error_message)

        video_converter_service_stub.execute = AsyncMock(side_effect=error)

        response = await video_to_audio_usecase.convert(video)

        assert response.success == False
        assert response.body == error_message