from unittest.mock import AsyncMock
import pytest_asyncio
from domain.services.mp3_file.mp3_file_service_interface import Mp3FileServiceInterface
from domain.usecases.mp3_file.mp3_file_impl import Mp3FileUseCase


class TestMp3FileUseCase:

    @pytest_asyncio.fixture
    def mp3_file_service_stub(self) -> Mp3FileServiceInterface:
        return AsyncMock(spec=Mp3FileServiceInterface)
    

    @pytest_asyncio.fixture
    def mp3_file_usecase(self, mp3_file_service_stub):
        return Mp3FileUseCase(mp3_file_service_stub)
    