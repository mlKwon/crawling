import numpy as np

def np_test(a:int):
    try:
        return np.array(a*2)
    except:
        return np.arange(5)