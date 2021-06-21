"""
정렬된 두 배열 A, B가 주어짐. 합친 후 정렬해서 출력하는 프로그램 작성.

첫줄엔 A의 크기 N, B의 크기 M.
둘째 줄엔 A의 내용, 셋째 줄엔 B의 내용.
"""
N, M = map(int, input().split())
listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

myList = sorted(listA + listB)

for i in range(len(myList)):
    print(myList[i], end=' ')

""" 
# 제출용
import sys

N, M = map(int, sys.stdin.readline().split())
listA = list(map(int, sys.stdin.readline().split()))
listB = list(map(int, sys.stdin.readline().split()))
myList = sorted(listA + listB)
for i in range(len(myList)):
    print(myList[i], end=' ')
"""