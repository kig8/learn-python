from bank import value


def test_start_with_h():
    assert value("hi") == 0
    assert value("What's up?") == 0
