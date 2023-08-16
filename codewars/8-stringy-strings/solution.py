# SOLUTION
def stringy(size):
    return ("10" * ((size // 2) + 1))[:size]


# TEST FUNCTION
def test_stringy():
    assert stringy(3) == "101"
    assert stringy(5) == "10101"
    assert stringy(12) == "101010101010"
    assert stringy(26) == "10101010101010101010101010"
    assert stringy(28) == "1010101010101010101010101010"
