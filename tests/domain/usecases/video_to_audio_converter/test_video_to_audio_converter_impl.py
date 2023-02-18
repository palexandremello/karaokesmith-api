import pytest
from unittest.mock import Mock
from domain.entities.audio_media import AudioFormat, AudioMedia
from domain.entities.video_source import VideoSource
from domain.services.video_converter.video_converter_service_interface import VideoConverterServiceInterface
from domain.usecases.video_to_audio_converter.video_to_audio_converter_impl import VideoToAudioConverterUseCase
from domain.utils.use_case_response import UseCaseResponse


class TestVideoToAudioConverterUseCase:

    @pytest.fixture
    def video_converter_service_stub(self) -> VideoConverterServiceInterface:
        return Mock(spec=VideoConverterServiceInterface)
    

    @pytest.fixture
    def video_to_audio_usecase(self, video_converter_service_stub):
        return VideoToAudioConverterUseCase(video_converter_service_stub)
    


    def test_should_return_an_AudioMedia_when_video_converter_is_success(self, video_to_audio_usecase,
                                                                         video_converter_service_stub):
        video = VideoSource(title="Real Estate - Paper Cup", thumbnail_url="any_thumbnail_url", path="any_path")
        audio = AudioMedia(path="any_path", audio_format= AudioFormat.MP3)

        video_converter_service_stub.execute.return_value = audio

        response = video_to_audio_usecase.convert(video)


        assert isinstance(response, UseCaseResponse)
        assert response.success
        assert response.body == audio

    
    def test_should_return_an_response_with_Exception_when_video_converter_has_failed(self, video_to_audio_usecase,
                                                                                      video_converter_service_stub):
        
        video = VideoSource(title="Real Estate - Paper Cup", thumbnail_url="any_thumbnail_url", path="any_path")
        error_message = "Error during audio conversion"

        video_converter_service_stub.execute.side_effect = Exception(error_message)

        response = video_to_audio_usecase.convert(video)

        assert response.success == False
        assert response.body == error_message