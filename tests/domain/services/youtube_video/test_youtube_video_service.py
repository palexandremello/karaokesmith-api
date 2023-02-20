

from unittest.mock import AsyncMock
import pytest
import pytest_asyncio

from domain.services.youtube_video.youtube_video_downloader_interface import YoutubeDownloaderInterface
from domain.services.youtube_video.youtube_video_service import YoutubeVideoService
from domain.services.youtube_video.youtube_video_service_interface import YoutubeVideoServiceInterface


class TestYoutubeVideoService:

    URL = "https://www.youtube.com/watch?v=CHKk8OozMfo"
    EXPECTED_VIDEO_INFO = {"title": "School Food Punishment - You May Crawl",
                           "thumbnail_url": "any_thumbnail_url"}

    @pytest_asyncio.fixture
    def youtube_video_downloader_stub(self) -> YoutubeDownloaderInterface:
        return AsyncMock(spec=YoutubeDownloaderInterface)
    

    @pytest_asyncio.fixture
    def youtube_video_service(self, youtube_video_downloader_stub) -> YoutubeVideoServiceInterface:
        return YoutubeVideoService(youtube_video_downloader=youtube_video_downloader_stub)
    


    @pytest.mark.asyncio
    async def test_should_be_able_to_get_video_info(self, 
                                                    youtube_video_downloader_stub: YoutubeDownloaderInterface,
                                                    youtube_video_service: YoutubeVideoServiceInterface):
        
        youtube_video_downloader_stub.get_video_info = AsyncMock(return_value=self.EXPECTED_VIDEO_INFO)

        video_metadata = await  youtube_video_service.get_info(url=self.URL)

        assert video_metadata == self.EXPECTED_VIDEO_INFO

    
    @pytest.mark.asyncio
    async def test_should_raises_KeyError_when_is_unable_to_get_video_info(self,
                                                                           youtube_video_downloader_stub: YoutubeDownloaderInterface,
                                                                           youtube_video_service: YoutubeVideoServiceInterface):
        
        youtube_video_downloader_stub.get_video_info = AsyncMock(return_value={})

        with pytest.raises(KeyError):
            await youtube_video_service.get_info(self.URL)