import pytest

from domain.entities.mp3_file import Mp3File
from domain.entities.sample import Sample
from domain.entities.youtube_audio import YoutubeAudio


class TestSample:
    EXPECTED_SAMPLE_DICTIONARY = {
        "name": "any_artist",
        "audio_option": {"name": "any_artist", "path": "any_path"},
        "content": b"bytes",
        "path": None,
    }

    @pytest.fixture
    def mp3_file_data(self):
        return Mp3File(name="any_artist", path="any_path")

    @pytest.fixture
    def youtube_audio_data(self, mp3_file_data):
        return YoutubeAudio(video_url="any_video_url", mp3_file=mp3_file_data)

    def test_should_be_able_to_create_a_Sample_from_dict(self, mp3_file_data):
        sample_dictionary = {"name": "any_artist", "audio_option": mp3_file_data}
        sut = Sample.from_dict(sample_dictionary)

        assert sut.name == self.EXPECTED_SAMPLE_DICTIONARY["name"]

    def test_should_be_able_to_returns_a_dict_from_Sample(self, mp3_file_data):
        sample_dictionary = {"name": "any_artist", "audio_option": mp3_file_data, "content": b"bytes", "path": None}
        sut = Sample.from_dict(sample_dictionary)

        assert sut.to_dict() == self.EXPECTED_SAMPLE_DICTIONARY

    def test_should_be_able_to_create_a_Sample_from_dict_and_return_dict_representation_when_is_YoutubeAudio(
        self, youtube_audio_data
    ):
        sample_dictionary = {
            "name": "any_artist",
            "audio_option": youtube_audio_data,
            "content": b"bytes",
            "path": None,
        }
        expected_dictionary_with_youtube_audio = {
            "name": "any_artist",
            "audio_option": youtube_audio_data.to_dict(),
            "content": b"bytes",
            "path": None,
        }
        sut = Sample.from_dict(sample_dictionary)

        assert sut.name == self.EXPECTED_SAMPLE_DICTIONARY["name"]
        assert sut.to_dict() == expected_dictionary_with_youtube_audio
