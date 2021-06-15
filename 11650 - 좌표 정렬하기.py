"""
x가 증가하는 순
x가 같으면 y가 증가하는 순으로 정렬.
"""
# 1초면 시간초과 뜰거같은데 ㅅㅂ
# N = int(input())

import sys

N = int(sys.stdin.readline())

myList = []

# x,y를 list형태로 한번에 받는다?
for i in range(N) :
    # [x, y] = map(int, input().split())
    [x, y] = map(int, sys.stdin.readline().split())
    myList.append([x, y])
    
# print(myList)

sortList = sorted(myList)
# print(sortList)

for i in range(len(sortList)):
    print(sortList[i][0], sortList[i][1])