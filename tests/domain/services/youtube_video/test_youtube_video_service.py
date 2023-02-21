

import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from domain.entities.video_metadata import VideoMetadata
from domain.entities.video_source import VideoSource
from domain.services.youtube_video.youtube_video_downloader_interface import YoutubeDownloaderInterface
from domain.services.youtube_video.youtube_video_service import YoutubeVideoService
from domain.services.youtube_video.youtube_video_service_interface import YoutubeVideoServiceInterface
from domain.utils.response import Response


class TestYoutubeVideoService:

    URL = "https://www.youtube.com/watch?v=CHKk8OozMfo"
    EXPECTED_RESPONSE = Response(success=True, body=VideoSource("School Food Punishment - You May Crawl",
                                                                "any_thumbnail_url", "any_path"))
    @pytest_asyncio.fixture
    def youtube_video_downloader_stub(self) -> YoutubeDownloaderInterface:
        return AsyncMock(spec=YoutubeDownloaderInterface)
    

    @pytest_asyncio.fixture
    def youtube_video_service(self, youtube_video_downloader_stub) -> YoutubeVideoServiceInterface:
        return YoutubeVideoService(youtube_video_downloader=youtube_video_downloader_stub)
    
    @pytest.mark.asyncio
    async def test_should_be_able_to_return_a_response_with_VideoSource_entity_when_YoutubeVideoService_successful(self, 
                                                    youtube_video_downloader_stub: YoutubeDownloaderInterface,
                                                    youtube_video_service: YoutubeVideoServiceInterface):
        
        youtube_video_downloader_stub.get_video_info = AsyncMock(return_value=VideoMetadata(title="School Food Punishment - You May Crawl",
                                                                                            thumbnail_url="any_thumbnail_url"))
        youtube_video_downloader_stub.get_video = AsyncMock(return_value="any_path")

        response = await  youtube_video_service.download(url=self.URL)

        assert response == self.EXPECTED_RESPONSE

    
    @pytest.mark.asyncio
    async def test_should_be_able_to_return_response_with_error_when_get_video_throws(self, 
                                youtube_video_downloader_stub: YoutubeDownloaderInterface,
                                youtube_video_service: YoutubeVideoServiceInterface):
        
        error_message = "any_error"
        error = KeyError(error_message)
        youtube_video_downloader_stub.get_video_info = AsyncMock(side_effect=error)

        response = await youtube_video_service.download(url=self.URL)
        
        assert response.success is False
        assert response.body == error