# SOLUTION
def solution(a, b):
    return f"{a}{b}{a}" if len(a) < len(b) else f"{b}{a}{b}"


# TEST FUNCTION
def test_solution():
    assert solution("45", "1") == "1451"
    assert solution("13", "200") == "1320013"
    assert solution("Soon", "Me") == "MeSoonMe"
    assert solution("U", "False") == "UFalseU"
