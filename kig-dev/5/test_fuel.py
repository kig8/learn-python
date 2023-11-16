from fuel import convert, gauge
import pytest


def test_convert():
    assert convert("4/4") == 100
    assert convert("4/10") == 40
    assert convert("0/10") == 0


def test_convert_errors():
    with pytest.raises(ValueError):
        convert("X/100")
    with pytest.raises(ValueError):
        convert("X/100")
    with pytest.raises(ValueError):
        convert("101/100")
    with pytest.raises(ValueError):
        convert("dog")
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_gauge():
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
    assert gauge(70) == "70%"
    assert gauge(2) == "2%"
