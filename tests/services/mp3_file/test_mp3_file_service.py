

from typing import Union
from unittest import mock 
from unittest.mock import MagicMock, Mock
from domain.services.mp3_file.mp3_file_service import Mp3FileService
from domain.services.mp3_file.mp3_file_validator_interface import Mp3FileValidatorInterface


class Mp3FileValidatorStub(Mp3FileValidatorInterface):
    def validate(self, path: str) -> Union[None, Exception]:
        return super().validate(path)



def mock_Mp3FileValidator_with_correct_validation():
    validator = Mp3FileValidatorStub()
    validator.validate = MagicMock(return_value=None)
    return validator

def mock_exception_Mp3FileValidator():
    validator = Mp3FileValidatorStub()
    validator.validate = Mock(side_effect=Exception("any_error"))
    return validator


def test_should_return_None_when_validate_is_correct():
    validator = mock_Mp3FileValidator_with_correct_validation()
    sut = Mp3FileService(validator)

    response = sut.validate_mp3_file("ANY_PATH")

    assert response is None


def test_should_raise_exception_when_validate_is_incorrect():
    validator = mock_exception_Mp3FileValidator()

    sut = Mp3FileService(validator)

    error = sut.validate_mp3_file("ANY_PATH")
    
    assert isinstance(error, Exception)
        
