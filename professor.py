import pytest
from app import video_link_format, video_download, video_file_type


def main():
    test_link_format()
    test_link_format_fail()
    test_video_download()


def test_link_format_fail():
    with pytest.raises(SystemExit):
        video_link_format("www.google.com")
        video_link_format("www.facebook.com")


def test_link_format():
    assert video_link_format("https://www.youtube.com/watch?v=QAUzWtLMnU0&t=7s") == \
           "https://www.youtube.com/watch?v=QAUzWtLMnU0&t=7s"
    assert video_link_format(
        "https://www.youtube.com/watch?v=rJNBGqiBI7s") == "https://www.youtube.com/watch?v=rJNBGqiBI7s"


def test_video_download():
    assert video_download("https://www.youtube.com/watch?v=QAUzWtLMnU0&t=7s") == "C:\\Users\William Ross\\PycharmProjects" \
                                                                                 "\\Hellloworld\\test_files\empty.mp4"


def test_video_file_type():
    pass