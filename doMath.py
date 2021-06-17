import numpy as np

def doMath(text):
    try:
        number = float(text)
        square = np.sqrt(number)
        return str(square)
    except:
        return f'{text} is not a number'
    # number = float(text)
    # square = np.sqrt(number)
    # return str(square)


# print(doMath('A'))


