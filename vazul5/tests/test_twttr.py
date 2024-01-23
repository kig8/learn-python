
from twttr import shorten



def test_sorten():

    assert shorten("Twitter") == "Twttr"

def test_shotren_upper():

    assert shorten("TWITTER") == "TWTTR"

def test_shorten_with_numbers():
    assert shorten('1234') == '1234'


