from app.domain.entities.video_source import VideoSource
from app.domain.usecases.get_youtube_video.get_youtube_video_interface import GetYoutubeVideoUseCaseInterface
from app.domain.services.youtube_video.youtube_video_service_interface import YoutubeVideoServiceInterface
from app.domain.utils.response import Response


class GetYoutubeVideoUseCase(GetYoutubeVideoUseCaseInterface):
    def __init__(self, youtube_video_service: YoutubeVideoServiceInterface) -> None:
        self.youtube_video_service = youtube_video_service

    async def get(self, video_url: str) -> Response[VideoSource]:
        response_video = await self.youtube_video_service.download(video_url)

        if response_video.success:
            video = response_video.body
            return Response(success=True, body=video)

        return Response(success=False, body=response_video.body)
