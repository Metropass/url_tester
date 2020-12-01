import os
import pytest

@pytest.fixture()
def testing_url_list():
    return ["https://youtube.ca", "https://gibhubfe.com/TASVideos", "http://www.danepstein.ca/category/open-source/feed"]

def testing_url_good(url_arg):
    urls = testing_url_list()
    a = os.system("python release0_1.py --url https://youtube.ca")
    assert (a) == 200

def test_url_404():
    urls = testing_url_list()
    a = os.system("python release0_1.py --url https://gibhubfe.com/TASVideos")
    assert (a) == 404

def test_url_403():
    urls = testing_url_list()
    a = os.system("python release0_1.py --url http://www.danepstein.ca/category/open-source/feed")
    assert (a) == 403

def error_check():
    url = "h://youtube.ca"
    a = os.system("python release0_1.py --url {}".format(url))
