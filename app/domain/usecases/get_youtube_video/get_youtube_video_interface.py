from abc import ABC, abstractmethod
from domain.entities.video_source import VideoSource

from domain.utils.use_case_response import UseCaseResponse


class GetYoutubeVideoUseCaseInterface(ABC):

    @abstractmethod
    async def get(self, url: str) -> UseCaseResponse[VideoSource]:
        pass