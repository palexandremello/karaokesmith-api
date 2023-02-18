

from unittest.mock import MagicMock
import pytest
from domain.entities.video_source import VideoSource
from domain.services.youtube_video.youtube_video_service_interface import YoutubeVideoServiceInterface
from domain.usecases.get_youtube_video.get_youtube_video_impl import GetYoutubeVideoUseCase

VIDEO_SOURCE_DICT = {"title": "School Food Punishment - RPG",
                     "thumbnail_url": "https://is2-ssl.mzstatic.com/image/thumb/Music124/v4/04/1b/c9" + 
                                      "/041bc9d9-dd4c-a23e-a985-2e617a362ec6/jacket_ESCL03670B00Z_550.jpg/1200x1200bf-60.jpg",
                     "path": "any_path"}

class YoutubeVideoServiceStub(YoutubeVideoServiceInterface):

    async def download(self, url: str) -> VideoSource:
        return VideoSource.from_dict(VIDEO_SOURCE_DICT)
    



class TestGetYoutubeVideoUseCase:

    @pytest.fixture
    async def youtube_video_service_mock(self):
        return YoutubeVideoServiceStub()
    
    @pytest.fixture
    async def get_youtube_video_usecase(self, youtube_video_service_mock):
        return GetYoutubeVideoUseCase(youtube_video_service_mock)
    
    async def test_get_youtube_video_with_a_valid_url(self, get_youtube_video_usecase):
        url = "https://www.youtube.com/watch?v=r6Xg8ldqC_4"

        response = await get_youtube_video_usecase.get(url)

        assert response.success
        assert response.body.to_dict() == VIDEO_SOURCE_DICT

    async def test_should_returns_a_response_with_error_when_url_is_incorrect(self, get_youtube_video_usecase, 
                                                                        youtube_video_service_mock):
        youtube_video_service_mock.download = MagicMock(side_effect=Exception("any_error"))
        url = "invalid_url"

        response = await get_youtube_video_usecase.get(url)

        assert not response.success
        assert response.body == "any_error"