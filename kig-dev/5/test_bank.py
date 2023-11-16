from bank import value


def test_start_with_hello():
    assert value("Hello there") == 0
    assert value("helloka") == 0


def test_start_with_h():
    assert value("hi") == 20
    assert value("How?") == 20
    assert value("hola!") == 20


def test_start_with_else():
    assert value("Yo") == 100
    assert value("What's up?") == 100
