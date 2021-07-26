from is_string.is_string import is_string


def test_is_string():
    assert is_string("")
    assert is_string(" ")
    assert is_string("t")
    assert is_string("test")
    assert is_string(str())


def test_is_not_string():
    assert not is_string(1)
    assert not is_string([])
    assert not is_string({})
    assert not is_string(int())
    assert not is_string(float())
