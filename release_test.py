import subprocess
import pytest

@pytest.fixture
def testing_url_data():
    return ['https://youtube.ca','https://gibhubfe.com/TASVideos','http://www.danepstein.ca/category/open-source/feed']

def testing_url_good(url_arg):
    urls = testing_url_list()
    a = call("python release0_1.py --url {}".format(urls[0]))
    assert (a) == 200

def test_url_404():
    urls = testing_url_list()
    a = call("python release0_1.py --url {}".format(urls[1]))
    assert (a) == 404

def test_url_403():
    urls = testing_url_list()
    a = call("python release0_1.py --url {}".format(urls[2]))
    assert (a) == 403

def error_check():
    url = "h://youtube.ca"
    a = call("python release0_1.py --url h://youtube.ca")
    assert (a) == -1
