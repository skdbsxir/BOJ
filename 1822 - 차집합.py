"""
집합 A와 B. A에는 속하면서 B에는 속하지 않는 모든 원소 구하기.
하나의 집합의 원소는 2,147,483,647 이하의 자연수

입력 : 첫줄엔 A의 원소갯수, B의 원소 갯수. (둘다 500,000 이하)
       둘째줄엔 A의 원소
       셋째줄엔 B의 원소
      
출력 : A에는 속하면서 B에는 속하지 않는 원소의 갯수 출력.
      그 다음줄엔 원소를 빈 칸 사이에 두고 증가하는 순으로 출력.
"""
import sys

# N, M = map(int, input().split())
N, M = map(int, sys.stdin.readline().split())

# setA = set(list(map(int, input().split())))
# setB = set(list(map(int, input().split())))
setA = set(list(map(int, sys.stdin.readline().split())))
setB = set(list(map(int, sys.stdin.readline().split())))

# print(setA)
# print(setB)

AmB = list(setA - setB)
AmB.sort()

print(len(AmB))
for i in range(len(AmB)):
    print(AmB[i], end=' ')
