import numpy as np
def adjacentElementsProduct(inputArray):
    a=[]
    for i in range(len(inputArray)-1):
        a.append(inputArray[i]*inputArray[i+1])
    return np.max(a)
