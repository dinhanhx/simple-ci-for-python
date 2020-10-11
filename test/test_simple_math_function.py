import sys
import numpy as np
try:
    sys.path.append('../src')
    from simple_math_function import *
except ImportError:
    sys.path.append('src')
    from simple_math_function import *

signalOne = np.array([1, 2, 3])
signalTwo = np.array([3, 2, 1])

def test_add():
    expectedSignal = np.array([4, 4, 4])
    assert np.array_equal(add_two_1D_signal(signalOne, signalTwo), expectedSignal)

def test_subtract():
    expectedSignal = np.array([-2, 0, 2])
    assert np.array_equal(subtract_two_1D_signal(signalOne, signalTwo), expectedSignal)

def test_multiply():
    expectedSignal = np.array([3, 4, 3])
    assert np.array_equal(multiply_two_1D_signal(signalOne, signalTwo), expectedSignal)

def test_divide():
    expectedSignal = np.array([1/3, 1/1, 3/1])
    assert np.array_equal(divide_two_1D_signal(signalOne, signalTwo), expectedSignal)
