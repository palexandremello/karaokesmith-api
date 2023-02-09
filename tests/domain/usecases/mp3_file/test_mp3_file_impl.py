
from typing import Union
from unittest.mock import MagicMock
from domain.entities.mp3_file import Mp3File
from domain.services.mp3_file.mp3_file_service_interface import Mp3FileServiceInterface
from domain.usecases.mp3_file.mp3_file_impl import Mp3FileUseCaseImpl


class Mp3FileServiceStub(Mp3FileServiceInterface):
    def validate_mp3_file(self, path: str) -> Union[Exception, None]:
        pass


def mockMp3FileServiceStub():
    mp3_file_service_stub = Mp3FileServiceStub()
    mp3_file_service_stub.validate_mp3_file = MagicMock(return_value=None)
    return mp3_file_service_stub

def mockExceptionMp3FileServiceStub():
    mp3_file_service_stub = Mp3FileServiceStub()
    mp3_file_service_stub.validate_mp3_file = MagicMock(return_value=Exception("invalid path"))
    return mp3_file_service_stub

def test_should_return_Mp3File_when_path_is_valid():
    mp3_file_service_stub = mockMp3FileServiceStub()
    sut = Mp3FileUseCaseImpl(mp3_file_service_stub)
    path = "any_path"
    mp3_file = sut.execute(path)

    assert isinstance(mp3_file, Mp3File)

    assert mp3_file.path == path

def test_should_return_Exception_when_path_is_invalid():
    mp3_file_service_stub = mockExceptionMp3FileServiceStub()
    sut = Mp3FileUseCaseImpl(mp3_file_service_stub)
    path = "any_path"

    error = sut.execute(path)

    assert isinstance(error, Exception)
