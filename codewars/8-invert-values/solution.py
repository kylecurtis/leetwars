# SOLUTION
def invert(lst):
    invert_lst = []
    for num in lst:
        invert_lst.append(-num)
    return invert_lst


# TEST FUNCTION
def test_invert():
    assert invert([1, 2, 3, 4, 5]) == [-1, -2, -3, -4, -5]
    assert invert([1, -2, 3, -4, 5]) == [-1, 2, -3, 4, -5]
    assert invert([]) == []
