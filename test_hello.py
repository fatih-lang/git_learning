from hello import add_numbers


def test_add_numbers():
    # Check that the function correctly adds two numbers.
    assert add_numbers(2, 3) == 5