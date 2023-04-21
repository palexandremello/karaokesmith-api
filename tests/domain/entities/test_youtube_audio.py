from app.domain.entities.mp3_file import Mp3File
from app.domain.entities.youtube_audio import YoutubeAudio


def test_should_create_a_YoutubeAudio_from_dict():
    youtube_audio_dict = {"video_url": "https://www.youtube.com/watch?v=b8E-r3ieWqY"}
    sut = YoutubeAudio.from_dict(youtube_audio_dict)

    assert sut.video_url == youtube_audio_dict["video_url"]
    assert sut.mp3_file is None


def test_should_returns_a_dictionary_from_YoutubeAudio_entity():
    youtube_audio_dict = {
        "video_url": "https://www.youtube.com/watch?v=b8E-r3ieWqY",
        "mp3_file": Mp3File(name="Dinosaur Jr - I Don't Think So", path="any_path"),
    }

    sut = YoutubeAudio.from_dict(youtube_audio_dict)

    youtube_audio_dicionary = sut.to_dict()

    assert youtube_audio_dicionary["video_url"] == youtube_audio_dict["video_url"]
    assert youtube_audio_dicionary["mp3_file"] == youtube_audio_dict["mp3_file"].to_dict()
