import asyncio
from tempfile import TemporaryDirectory
from yt_dlp import YoutubeDL
from domain.entities.video_metadata import VideoMetadata

from domain.services.youtube_video.youtube_video_downloader_interface import (
    YoutubeDownloaderInterface,
)


class YtDlpVideoDownloader(YoutubeDownloaderInterface):
    def __init__(self) -> None:
        self._tmp_dir = TemporaryDirectory().name
        self.__options = {"outtmpl": f"{self._tmp_dir}/%(id)s%(ext)s"}
        self.youtube_dl: YoutubeDL = YoutubeDL(self.__options)

    async def get_video(self, video_url: str) -> str:
        pass

    async def get_video_info(self, video_url: str) -> VideoMetadata:
        with self.youtube_dl:
            result = await asyncio.get_event_loop().run_in_executor(
                None, lambda: self.youtube_dl.extract_info(video_url, download=False)
            )

        if result.keys() is None:
            raise KeyError("any video metadata")

        return VideoMetadata(title=result["title"], thumbnail_url=result["thumbnail"])
