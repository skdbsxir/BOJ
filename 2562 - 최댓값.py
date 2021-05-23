"""
9개의 서로 다른 자연수를 입력.
이 중 최댓값 찾고
그 수가 몇번째인지?
"""

# 백준에서 넘파이 못쓰네 ㅋㅋ;;
"""
import numpy as np

myArray = np.arange(0, 9)
for i in range(9) :
    #myList.append(int(input()))
    myArray[i] = int(input())
    
#print('\n')
#print(myArray)
#print(myArray[0])
print(np.max(myArray))

# 최댓값이 있는 인덱스.
# print(np.argmax(myArray))   
maxIndex = np.argmax(myArray) + 1
print(maxIndex)
"""

myList = []
for i in range(9) :
    myList.append(int(input()))
    
print(max(myList))
# 리스트의 index 찾기? [].index('찾고자 하는 아이템') --> 아이템의 index 반환.
print(myList.index(max(myList)) + 1)