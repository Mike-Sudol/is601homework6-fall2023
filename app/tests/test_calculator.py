""" Test Calculator Operations """
from app.calculator import Calculator

def test_addition():
    '''Test that addition function works '''    
    assert Calculator.add(2,2) == 4

def test_addition2():
    '''Test that addition function works '''    
    assert Calculator.add(5,6) == 11

def test_subtraction():
    '''Test that addition function works '''    
    assert Calculator.subtract(2,2) == 0

def test_subtraction2():
    '''Test that addition function works '''    
    assert Calculator.subtract(152,145) == 7

def test_divide():
    '''Test that division function works '''    
    assert Calculator.divide(2,2) == 1

def test_divide2():
    '''Test that division function works '''    
    assert Calculator.divide(15,3) == 5

def test_multiply():
    '''Test that multiply function works '''    
    assert Calculator.multiply(2,2) == 4

def test_multiply2():
    '''Test that multiply function works '''    
    assert Calculator.multiply(7,5) == 35
