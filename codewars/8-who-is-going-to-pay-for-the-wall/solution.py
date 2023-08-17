# SOLUTION
def who_is_paying(name):
    return [name] if len(name) < 3 else [name, name[:2]]


# TEST FUNCTION
def test_who_is_paying():
    assert who_is_paying("Mexico") == ["Mexico", "Me"]
    assert who_is_paying("Melania") == ["Melania", "Me"]
    assert who_is_paying("Melissa") == ["Melissa", "Me"]
    assert who_is_paying("Me") == ["Me"]
    assert who_is_paying("") == [""]
    assert who_is_paying("I") == ["I"]
