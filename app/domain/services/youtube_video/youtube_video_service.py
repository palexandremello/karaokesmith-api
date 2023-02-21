from domain.entities.video_source import VideoSource
from domain.services.youtube_video.youtube_video_downloader_interface import YoutubeDownloaderInterface
from domain.services.youtube_video.youtube_video_service_interface import YoutubeVideoServiceInterface
from domain.utils.response import Response


class YoutubeVideoService(YoutubeVideoServiceInterface):

    def __init__(self, youtube_video_downloader: YoutubeDownloaderInterface) -> None:
        self.youtube_video_downloader = youtube_video_downloader
    

    async def download(self, url: str) -> Response[VideoSource]:
        try:
            video_metadata = await self.youtube_video_downloader.get_video_info(url)
            path = await self.youtube_video_downloader.get_video(url)
            video = VideoSource(title=video_metadata.title, 
                                thumbnail_url=video_metadata.thumbnail_url,
                                path=path)
            return Response(success=True, body=video)
        except KeyError as error:
            return Response(success=True, body=str(error))