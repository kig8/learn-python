from twttr import shorten


def test_twttr():
    assert shorten("KoVacsIstvanGELLERT") == "KVcsstvnGLLRT"
