import pytest
from src.calculator import *

def test_calculator_creation():
    assert Calculator() is not None


add_cases = [
    (1, 1, 2),
    (1, 2, 3),
    (100, 100, 200),
    (2000, 10, 2010),
    (222, 111, 333),
    (200, -200, 0)
]


def test_addition_one_one():
    assert Calculator().add(1, 1) == 2


def test_addition_one_two():
    assert Calculator().add(1, 2) == 3

@pytest.mark.parametrize('a,b,result', add_cases)
def test_addition_parametrized(a,b, result):
    assert Calculator().add(a,b) == result
