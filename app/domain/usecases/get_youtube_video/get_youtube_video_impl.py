from domain.entities.video_source import VideoSource
from domain.usecases.get_youtube_video.get_youtube_video_interface import GetYoutubeVideoUseCaseInterface
from domain.services.youtube_video.youtube_video_service_interface import YoutubeVideoServiceInterface
from domain.utils.response import Response


class GetYoutubeVideoUseCase(GetYoutubeVideoUseCaseInterface):
    def __init__(self, youtube_video_service: YoutubeVideoServiceInterface) -> None:
        self.youtube_video_service = youtube_video_service

    async def get(self, video_url: str) -> Response[VideoSource]:
        try:
            video = await self.youtube_video_service.download(video_url)

            return Response(success=True, body=video)

        except Exception as error:
            return Response(success=False, body=str(error))
