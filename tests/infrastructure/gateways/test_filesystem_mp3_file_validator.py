

from unittest.mock import mock_open, patch
from infrastructure.gateways.filesystem_mp3_file_validator import FileSystemMp3FileValidator


def test_should_return_exception_when_file_not_found():
    sut = FileSystemMp3FileValidator()

    error = sut.validate("ANY_PATH")

    assert isinstance(error, FileNotFoundError)


def test_should_return_exception_when_mp3_mime_type_is_incorrect(mocker):
    mocker.patch("os.path.exists")

    sut = FileSystemMp3FileValidator()

    error = sut.validate("ANY_PATH")

    assert isinstance(error, ValueError)


def test_should_return_exception_when_mp3_file_is_invalid(mocker):
    mocker.patch("os.path.exists")
    sut = FileSystemMp3FileValidator()

    error = sut.validate("any.mp3")

    assert isinstance(error, ValueError)

def test_should_return_None_when_mp3_file_is_correct(mocker):
    mocker.patch("os.path.exists")
    with patch("builtins.open", mock_open(read_data=b'ID3')) as mock_file:
        sut = FileSystemMp3FileValidator()
        validation = sut.validate("any.mp3")
        assert validation is None
    assert mock_file.called


def test_should_return_exception_when_mp3_ID3_is_incorrect(mocker):
    mocker.patch("os.path.exists")
    with patch("builtins.open", mock_open(read_data=b'ID20')) as mock_file:

        sut = FileSystemMp3FileValidator()
        error = sut.validate("any.mp3")
        assert isinstance(error, ValueError)
    
    assert mock_file.called
