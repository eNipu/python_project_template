import pytest
from src.service.calculator import Calculator

#write your tests here
def test_add():
    calc = Calculator()
    assert calc.add(2, 2) == 4, "2 + 2 should equal 4"

def test_subtract():
    calc = Calculator()
    assert calc.subtract(2, 2) == 0, "2 - 2 should equal 0"

def test_multiply():
    calc = Calculator()
    assert calc.multiply(2, 2) == 4, "2 * 2 should equal 4"

def test_divide():
    calc = Calculator()
    assert calc.divide(2, 2) == 1, "2 / 2 should equal 1"

def test_square_root():
    calc = Calculator()
    assert calc.square_root(4) == 2, "4 should equal 2"

def test_square():
    calc = Calculator()
    assert calc.square(4) == 16, "4 should equal 16"

def test_cube():
    calc = Calculator()
    assert calc.cube(4) == 64, "4 should equal 64"

def test_power():
    calc = Calculator()
    assert calc.power(2, 2) == 4, "2 ^ 2 should equal 4"

def test_modulus():
    calc = Calculator()
    assert calc.modulus(2, 2) == 0, "2 % 2 should equal 0"

def test_logarithm():
    calc = Calculator()
    assert calc.logarithm(4) == 1.3862943611198906, "4 should equal 1.3862943611198906"

def test_sine():
    calc = Calculator()
    assert calc.sine(4) == -0.7568024953079282, "4 should equal -0.7568024953079282"

def test_cosine():
    calc = Calculator()
    assert calc.cosine(4) == -0.6536436208636119, "4 should equal -0.6536436208636119"

def test_tangent():
    calc = Calculator()
    assert calc.tangent(4) == 1.1578212823495775, "4 should equal 0"

