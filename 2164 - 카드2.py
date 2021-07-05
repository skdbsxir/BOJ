"""
2161 카드1과 동일
입력 동일. 범위가 더 늘음.
출력은 마지막 남는 카드 번호만.
"""
"""
import sys
# import time

# start = time.time()
# N = int(input())
N = int(sys.stdin.readline())

myCard = [i+1 for i in range(N)]
    
# 1번카드가 제일위에 있으니
# 역순으로 두면 되지않을까.
myCard.sort(reverse=True)

# 1. 제일 위 카드 pop
# 2. 제일 위 카드를 맨 밑으로 이동
# 3. 1,2 과정을 반복
# 4. 마지막 남는 카드
while len(myCard) != 1:
    # 제일 위 카드 pop
    myCard.pop()
    
    # 제일 위 카드를 밑으로 이동
    myCard.insert(0, myCard[-1])
    myCard.pop()
    # 이 과정 반복
# stop = time.time()

# print(myCard[0])
# print('총 걸린시간? (ns) ', stop-start)
sys.stdout.write(myCard[0])
"""
# 그냥 Deque 쓰자... 정렬할 필요도 없고.
from collections import deque
import sys

N = int(sys.stdin.readline())
# N = int(input())
myCard = deque([i+1 for i in range(N)])

# print(myCard)
while len(myCard) != 1:
    # 맨 위(맨 왼쪽) 카드 빼고
    myCard.popleft()
    # 그 아래 장을 맨 아래로
    myCard.append(myCard.popleft())
     
print(myCard[0])
# sys.stdout.write(myCard[0])