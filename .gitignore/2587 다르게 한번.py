import sys
import numpy as np

myList = np.array(input())
# myList = np.array(map(int, myList))

"""
for i in range(0, myList.size):
    if myList[i] >= 100 :
        sys.exit(0)
    elif (myList[i] % 10) != 0 :
        sys.exit(0)
"""
a = myList.mean()
b = np.median(myList)
print(a, b)