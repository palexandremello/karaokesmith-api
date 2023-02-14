

from domain.usecases.youtube_audio.youtube_audio_impl import YoutubeAudioUseCaseImpl
from domain.usecases.youtube_audio.youtube_audio_interface import YoutubeAudioUseCaseInterface


def test_should_YoutubeAudioUseCaseImpl_same_instance_of_YoutubeAudioUseCaseInterface():

    sut = YoutubeAudioUseCaseImpl()

    assert isinstance(sut, YoutubeAudioUseCaseInterface)