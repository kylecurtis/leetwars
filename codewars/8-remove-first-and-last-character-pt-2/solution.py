# SOLUTION
def array(string):
    vals = string.split(",")
    return None if len(vals) < 3 else " ".join(vals[1:-1])


# TEST FUNCTION
def test_array():
    assert array("1,2,3") == "2"
    assert array("1,2,3,4") == "2 3"
    assert array("1,2,3,4,5") == "2 3 4"
    assert array("") == None
    assert array("1") == None
    assert array("1,2") == None
