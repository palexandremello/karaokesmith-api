from unittest.mock import AsyncMock
import pytest
import pytest_asyncio
from app.domain.entities.mp3_file import Mp3File
from app.domain.services.mp3_file.mp3_file_service_interface import Mp3FileServiceInterface
from app.domain.usecases.mp3_file.mp3_file_impl import Mp3FileUseCase
from app.domain.usecases.mp3_file.mp3_file_interface import Mp3FileUseCaseInterface


class TestMp3FileUseCase:
    MP3_DICT = {"name": "森高千里 『ザ・ストレス -ストレス 中近東バージョン-』", "path": "any_path"}

    @pytest_asyncio.fixture
    def mp3_file_service_stub(self) -> Mp3FileServiceInterface:
        return AsyncMock(spec=Mp3FileServiceInterface)

    @pytest_asyncio.fixture
    def mp3_file_usecase(self, mp3_file_service_stub: Mp3FileServiceInterface) -> Mp3FileUseCaseInterface:
        return Mp3FileUseCase(mp3_file_service_stub)

    @pytest.mark.asyncio
    async def test_should_return_Mp3File_when_path_is_valid(
        self, mp3_file_usecase: Mp3FileUseCaseInterface, mp3_file_service_stub: Mp3FileServiceInterface
    ):
        mp3_file_service_stub.validate_mp3_file = AsyncMock(return_value=None)

        response = await mp3_file_usecase.execute(self.MP3_DICT["name"], self.MP3_DICT["path"])

        assert response.success
        assert response.body == Mp3File.from_dict(self.MP3_DICT)

    @pytest.mark.asyncio
    async def test_should_return_Exception_when_path_is_invalid(
        self, mp3_file_usecase: Mp3FileUseCaseInterface, mp3_file_service_stub: Mp3FileServiceInterface
    ):
        expected_error = Exception("invalid mp3 file")
        mp3_file_service_stub.validate_mp3_file = AsyncMock(side_effect=expected_error)

        response = await mp3_file_usecase.execute(self.MP3_DICT["name"], self.MP3_DICT["path"])

        assert not response.success
        assert response.body == str(expected_error)
