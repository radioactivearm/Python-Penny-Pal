import numpy as np

def doMath(text):
    try:
        number = float(text)
        square = np.sqrt(number)
        rounded = round(square, 3)
        return str(rounded)
    except:
        return 'NAN'
    # number = float(text)
    # square = np.sqrt(number)
    # return str(square)


# print(doMath('A'))


