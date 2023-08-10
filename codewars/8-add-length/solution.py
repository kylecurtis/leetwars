# SOLUTION
def add_length(str_):
    word_list = str_.split()
    word_group = [f"{word} {len(word)}" for word in word_list]
    return word_group

# TEST FUNCTION
def test_add_length():
    assert add_length('apple ban') == ["apple 5", "ban 3"]
    assert add_length('you will win') == ["you 3", "will 4", "win 3"]
    assert add_length('you') == ["you 3"]
    assert add_length('y') == ["y 1"]
