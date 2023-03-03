import pytest
from src.calculator import *

def test_calculator_creation():
    assert Calculator() is not None