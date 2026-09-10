from calculator import add

# def test_add():
#     assert add(5, 5) == 10

# Multiple Test Cases
def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-2, -3) == -5


def test_add_zero():
    assert add(10, 0) == 10