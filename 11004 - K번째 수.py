"""
수 N개가 주어지고 오름차순 정렬.
앞에서 K번째에 있는 수 찾기
"""
# sys 안쓰면 메모리 터질라함.
import sys

# N, K = map(int, input().split())
N, K = map(int, sys.stdin.readline().split())
# myList = list(map(int, input().split()))
myList = list(map(int, sys.stdin.readline().split()))

myList.sort()

print(myList[K-1])