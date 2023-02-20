from domain.entities.video_source import VideoSource
from domain.services.youtube_video.youtube_video_downloader_interface import YoutubeDownloaderInterface
from domain.services.youtube_video.youtube_video_service_interface import YoutubeVideoServiceInterface


class YoutubeVideoService(YoutubeVideoServiceInterface):

    def __init__(self, youtube_video_downloader: YoutubeDownloaderInterface) -> None:
        self.youtube_video_downloader = youtube_video_downloader
    

    async def download(self, url: str) -> VideoSource:
        return url    

    async def get_info(self, url: str) -> dict:
        video_metadata = await  self.youtube_video_downloader.get_video_info(url)
        
        if not video_metadata:
            raise KeyError("Video does not exists or invalid url")
        
        return video_metadata

