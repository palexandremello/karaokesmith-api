import pytest

from domain.entities.mp3_file import Mp3File

def test_mp3_file_from_dict():
    mp3_dict = {"name": "森高千里 『ザ・ストレス -ストレス 中近東バージョン-』",
                "path": "any_path"}

    sut = Mp3File.from_dict(mp3_dict)

    assert sut.name == mp3_dict["name"]
    assert sut.path == mp3_dict["path"]