import numpy as np

def add_two_1D_signal(signalOne, signalTwo):
    return np.add(signalOne, signalTwo)

def subtract_two_1D_signal(signalOne, signalTwo):
    return np.subtract(signalOne, signalTwo)

def multiply_two_1D_signal(signalOne, signalTwo):
    return np.multiply(signalOne, signalTwo)

def divide_two_1D_signal(signalOne, signalTwo):
    return np.divide(signalOne, signalTwo)

if __name__ == '__main__':
    signalOne = np.array([1, 2, 3])
    signalTwo = np.array([3, 2, 1])
    print(add_two_1D_signal(signalOne, signalTwo))
    print('===')
    print(subtract_two_1D_signal(signalOne, signalTwo))
    print('===')
    print(multiply_two_1D_signal(signalOne, signalTwo))
    print('===')
    print(divide_two_1D_signal(signalOne, signalTwo))
