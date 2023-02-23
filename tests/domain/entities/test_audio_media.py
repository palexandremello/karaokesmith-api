from domain.entities.audio_media import AudioMedia


AUDIO_MEDIA_DICTIONARY = {"path": "any_path", "audio_format": "mp3"}


def test_should_create_a_AudioMedia_from_dict():
    sut = AudioMedia.from_dict(AUDIO_MEDIA_DICTIONARY)

    assert sut.path == AUDIO_MEDIA_DICTIONARY["path"]
    assert sut.audio_format == AUDIO_MEDIA_DICTIONARY["audio_format"]


def test_should_returns_a_dictionary_from_AudioMedia_entity():
    sut = AudioMedia.from_dict(AUDIO_MEDIA_DICTIONARY)

    audio_media_dict = sut.to_dict()

    assert audio_media_dict["path"] == AUDIO_MEDIA_DICTIONARY["path"]
    assert audio_media_dict["audio_format"] == AUDIO_MEDIA_DICTIONARY["audio_format"].value
