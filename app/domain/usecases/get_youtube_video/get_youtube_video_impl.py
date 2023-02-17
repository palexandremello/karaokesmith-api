

from domain.entities.video_source import VideoSource
from domain.usecases.get_youtube_video.get_youtube_video_interface import GetYoutubeVideoUseCaseInterface
from domain.services.youtube_video.youtube_video_service_interface import YoutubeVideoServiceInterface
from domain.utils.use_case_response import UseCaseResponse


class GetYoutubeVideoUseCase(GetYoutubeVideoUseCaseInterface):

    def __init__(self, youtube_video_service: YoutubeVideoServiceInterface) -> None:
        self.youtube_video_service = youtube_video_service

    def get(self, url: str) -> UseCaseResponse[VideoSource]:
        try:
            video = self.youtube_video_service.download(url)

            return UseCaseResponse(success=True, body=video)
        
        except Exception as error:
            return UseCaseResponse(success=False, body=str(error))