


from domain.entities.video_source import VideoSource

VIDEO_SOURCE_DICT = {"title": "looking over your city at 3am (Post-Punk playlist)",
                         "thumbnail_url": "any_thumbnail_url",
                         "path": "any_path"}


def test_should_create_a_VideoSource_from_dict():

    sut = VideoSource.from_dict(VIDEO_SOURCE_DICT)

    assert sut.title == VIDEO_SOURCE_DICT["title"]
    assert sut.thumbnail_url == VIDEO_SOURCE_DICT["thumbnail_url"]
    assert sut.path == VIDEO_SOURCE_DICT["path"]


def test_should_returns_a_dictionary_from_VideoSource_entity():

    sut = VideoSource.from_dict(VIDEO_SOURCE_DICT)

    video_source_dictionary = sut.to_dict()

    assert video_source_dictionary["title"] == VIDEO_SOURCE_DICT["title"]
    assert video_source_dictionary["thumbnail_url"] == VIDEO_SOURCE_DICT["thumbnail_url"]
    assert video_source_dictionary["path"] == VIDEO_SOURCE_DICT["path"]
