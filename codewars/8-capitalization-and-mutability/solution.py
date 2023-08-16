# SOLUTION
def capitalize_word(word):
    return word.capitalize()


# TEST FUNCTION
def test_capitalize_word():
    assert capitalize_word("word") == "Word"
    assert capitalize_word("i") == "I"
    assert capitalize_word("glasswear") == "Glasswear"
