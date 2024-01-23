from jar import Jar
from unittest.mock import MagicMock
import pytest


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(10)
    assert jar.size == 11
    with pytest.raises(ValueError) as err:
        jar.deposit(2)
    assert err.value.args[0] == "Too many cookie in the Jar"


def test_withdraw():
    jar = Jar()
    jar.deposit(3)
    with pytest.raises(ValueError) as err:
        jar.withdraw(4)
    assert err.value.args[0] == "Not enough cookie in the Jar"
