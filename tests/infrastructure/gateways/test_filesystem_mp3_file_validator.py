import os
import aiofiles
import pytest
import pytest_asyncio
from infrastructure.gateways.filesystem_mp3_file_validator import FileSystemMp3FileValidator
from unittest.mock import MagicMock, mock_open, patch
from aiofiles import threadpool

aiofiles.threadpool.wrap.register(MagicMock)(lambda *args, **kwargs: threadpool.AsyncBufferedIOBase(*args, **kwargs))


class TestFilesystemMp3FileValidator:
    PATH = "any_path/any_music.mp3"

    @pytest.fixture
    def os_exists_mock(self):
        with patch.object(os.path, "exists", MagicMock(return_value=True)) as os_exists_mock:
            yield os_exists_mock

    @pytest_asyncio.fixture
    def validator(self) -> FileSystemMp3FileValidator:
        return FileSystemMp3FileValidator()

    @pytest.mark.asyncio
    async def test_should_not_raise_when_validating_a_valid_file(self, validator, os_exists_mock):
        with patch("aiofiles.threadpool.sync_open", mock_open(read_data=b"ID3")) as open_mock:
            await validator.validate(self.PATH)

    @pytest.mark.asyncio
    async def test_should_raises_FileNotFoundError_when_path_is_incorrect(self, validator):
        with pytest.raises(FileNotFoundError):
            await validator.validate(self.PATH)

    @pytest.mark.asyncio
    async def test_should_return_exception_when_mp3_mime_type_is_incorrect(self, validator, os_exists_mock):
        with pytest.raises(ValueError):
            await validator.validate("any_path")

    @pytest.mark.asyncio
    async def test_should_return_exception_when_mp3_ID3_is_incorrect(self, validator, os_exists_mock):
        with patch("aiofiles.threadpool.sync_open", mock_open(read_data=b"ID20")) as open_mock:
            with pytest.raises(ValueError):
                await validator.validate(self.PATH)
