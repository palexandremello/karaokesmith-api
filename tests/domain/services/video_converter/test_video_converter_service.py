import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from domain.entities.audio_media import AudioFormat, AudioMedia
from domain.entities.video_source import VideoSource
from domain.services.video_converter.converter_interface import ConverterInterface
from domain.services.video_converter.video_converter_service import VideoConverterService
from domain.services.video_converter.video_converter_service_interface import VideoConverterServiceInterface


class TestVideoConverterService:

    @pytest_asyncio.fixture
    def converter_stub(self) -> ConverterInterface:
        return AsyncMock(spec=ConverterInterface)
    
    @pytest_asyncio.fixture
    def video_converter_service(self, converter_stub) -> VideoConverterServiceInterface:
        return VideoConverterService(converter=converter_stub)
    

    @pytest.mark.asyncio
    async def test_should_be_able_to_return_a_response_when_execute_is_successful(self,
                                                                            converter_stub: ConverterInterface,
                                                                            video_converter_service: VideoConverterServiceInterface):
        
        video_source = VideoSource(title="any_title",
                                   thumbnail_url="thumbnail_url",
                                   path="any_path")
        
        converter_stub.execute = AsyncMock(return_value="any_path")

        response = await video_converter_service.execute(video_source)

        assert response.success
        assert response.body == AudioMedia(path="any_path", audio_format=AudioFormat.MP3)


    @pytest.mark.asyncio
    async def test_should_be_able_to_return_a_response_when_execute_throws(self,
                                                                            converter_stub: ConverterInterface,
                                                                            video_converter_service: VideoConverterServiceInterface):
        converter_stub.execute = AsyncMock(side_effect=Exception("any_error"))

        response = await video_converter_service.execute("any_video_source")

        assert not response.success
        assert response.body == "any_error"