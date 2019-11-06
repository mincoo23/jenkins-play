from functions import my_sum, my_subtract, my_divide, my_multiply


def test_my_sum():
    a = 5
    b = 7
    assert my_sum(a, b) == 12


def test_my_subtract():
    a = 5
    b = 7
    assert my_subtract(a, b) == -2


def test_my_divide():
    a = 10
    b = 2
    assert my_divide(a, b) == 5.0


def test_my_multiply():
    a = 5
    b = 7
    assert my_multiply(a, b) == 35
