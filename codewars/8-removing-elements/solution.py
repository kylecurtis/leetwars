# SOLUTION
def remove_every_other(my_list):
    return my_list[::2]


# TEST FUNCTION
def test_remove_every_other():
    assert remove_every_other(["Hello", "Goodbye", "Hello Again"]) == [
        "Hello", "Hello Again"]
    assert remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [
        1, 3, 5, 7, 9]
    assert remove_every_other([["Goodbye"], {"Great": "Job"}]) == [["Goodbye"]]
