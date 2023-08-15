# SOLUTION
def say_hello(name, city, state):
    return f"Hello, {' '.join(name)}! Welcome to {city}, {state}!"


# TEST FUNCTION
def test_say_hello():
    assert (
        say_hello(["John", "Smith"], "Phoenix", "Arizona")
        == "Hello, John Smith! Welcome to Phoenix, Arizona!"
    )
    assert (
        say_hello(["Franklin", "Delano", "Roosevelt"], "Chicago", "Illinois")
        == "Hello, Franklin Delano Roosevelt! Welcome to Chicago, Illinois!"
    )
    assert (
        say_hello(["Wallace", "Russel", "Osbourne"], "Albany", "New York")
        == "Hello, Wallace Russel Osbourne! Welcome to Albany, New York!"
    )
    assert (
        say_hello(["Lupin", "the", "Third"], "Los Angeles", "California")
        == "Hello, Lupin the Third! Welcome to Los Angeles, California!"
    )
    assert (
        say_hello(["Marlo", "Stanfield"], "Baltimore", "Maryland")
        == "Hello, Marlo Stanfield! Welcome to Baltimore, Maryland!"
    )
