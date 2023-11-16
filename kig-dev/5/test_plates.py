from plates import is_valid


def test_start_two_letter():
    assert is_valid("Aa222") == True
    assert is_valid("z2222") == False
    assert is_valid("AA") == True


def test_length():
    assert is_valid("Aa2220") == True
    assert is_valid("Aa220") == True
    assert is_valid("A") == False
    assert is_valid("z222222") == False


def test_num_correct():
    assert is_valid("Aa0220") == False
    assert is_valid("aa2201") == True
    assert is_valid("Aaaaaa") == True
    assert is_valid("zz1000") == True
    assert is_valid("zz10z0") == False
    assert is_valid("zz1z10") == False
    assert is_valid("zz1lza") == False


def test_not_allowed():
    assert is_valid("Aa122.") == False
    assert is_valid("aa.2") == False
    assert is_valid("Aa:10") == False
    assert is_valid("zz,zz") == False
    assert is_valid("AA;") == False
    assert is_valid("AA ") == False
