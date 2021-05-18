import sys
import random

N = int(input())

myList = []
for i in range(N) :
    #myInput = sys.stdin.readlines()
    #myList.append(myInput[0])
    #myList = list(map(int, sys.stdin.readlines()))
    #myList.append(int(input()))
    myList.append(int(sys.stdin.readline()))
    
if len(myList) != N :
    sys.exit(0)
    
def quickSort(x) :
    # 랜덤으로 pivot을 하나 고르고
    # pivot을 기준으로 좌우로 나누고
    # 정렬되지 않은 좌우를 동일한 방법으로 나눈다.
    
    # List 길이가 1보다 작거나 같으면 List 자체를 반환.
    if len(x) <= 1:
        return x
    
    pivot = random.choice(x)
    
    lessThan = [i for i in x if i < pivot]
    moreThan = [i for i in x if i > pivot]
    
    sortLess = quickSort(lessThan)
    sortMore = quickSort(moreThan)
    
    return sortLess + [pivot] + sortMore

ansList = quickSort(myList)
"""
for i in range(len(ansList)) :
    #print(ansList[i], end='\n')
    sys.stdout.write(ansList(i)+'\n')
"""
for i in ansList :
    print(i)
#print(myList[::-1])

#print(type(myList[::-1]))