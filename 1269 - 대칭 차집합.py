"""
두 집합 A, B
A-B와 B-A의 합집합을 A와 B의 대칭차집합 이라 함.

입력 : A의 원소, B의 원소 개수 // A의 원소, B의 원소
출력 : 대칭 차집합의 원소 갯수
"""
import sys

# N, M = map(int, input().split())
N, M = map(int, sys.stdin.readline().split())

# listA = set(list(map(int, input().split())))
# listB = set(list(map(int, input().split())))
listA = set(list(map(int, sys.stdin.readline().split())))
listB = set(list(map(int, sys.stdin.readline().split())))

# print(listA)
# print(listB)

# A-B와 B-A를 구하면 되지않을까
AmB = listA - listB
# print(AmB)
BmA = listB - listA
# print(BmA)

ans = AmB.union(BmA)
print(len(ans))