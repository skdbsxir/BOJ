"""
카드는 1부터 N까지 적혀있음. 기술 3가지

1. 제일 위 카드 1장을 바닥에 둔다.
2. 위에서 두번째 카드를 바닥에 둔다. 카드 2장 이상일때만 가능.
3. 제일 밑에 있는 카드를 바닥에 둔다. 카드 2장 이상일때만 가능.

기술을 N번 써서 카드를 다 내려놨더니 위에서부터 순서대로 1,2,...,N.

처음 카드의 상태는 어땟을까

입력 : 첫줄엔 N
      둘째줄엔 길이 N인 수열 A.
          Ai = x : i번째로 카드를 내려놓을때 x번 기술을 썼다.
          Ai는 1,2,3중 하나이고, An은 항상 1.
출력 : 초기 카드 상태를 위에서부터 순서대로.
"""
from collections import deque
import sys

# N = int(input())
N = int(sys.stdin.readline())
# orderList = list(map(int, input().split())) # 명령리스트
orderList = list(map(int, sys.stdin.readline().split()))
myDeque = deque([i+1 for i in range(N)]) # 덱 생성

# print(orderList)
# print(myDeque)

# 덱의 맨 앞 == 카드의 맨 위?
# 덱의 맨 뒤 == 카드의 맨 위?
# 5 1 1 1 1 1 --> 5 4 3 2 1 인거 보니 맨뒤==맨위 인듯.
"""
def skill1(sampleDeque):
    return sampleDeque.pop()

# 위에서 두번째 카드 == 덱의 맨 뒤에서 두번째 원소
def skill2(sampleDeque):
    sampleDeque.rotate(1) # 맨 윗장은 그대로 두고 
    a = sampleDeque.pop() # 뒤에서 두번째 장 빼고
    # sampleDeque.rotate(-1) # 다시 원위치
    return a # 반환값은 뺀것.

def skill3(sampleDeque):
    return sampleDeque.popleft() # 제일 밑에 있는 카드를 바닥에 둔다.
"""
# 함수 쓸 필요가 없을듯 이거도.
# 입력받은 순서대로 명령을 실행하면 2 3 3 2 1 --> 1 5 2 3 4
# 명령의 맨 뒤부터 순서대로 실행하면 원래의 카드 순서가 나온다는 소린가
    # 맞네 ㅅㅂ

# 괜히 리스트 써서 꼬이지 말고 덱 쓰자
initialCard = deque()

# orderList 비울때까지 loop
while len(orderList) != 0:
    skill = orderList.pop()
    if skill == 1:
        # 1. 제일 위 카드 1장을 바닥에 둔다.
        # 역으로 보면 덱 맨앞이 초기 맨 뒤에 있는 셈.
        initialCard.appendleft(myDeque.popleft())
    elif skill == 2:
        # 2. 위에서 두번째 카드를 바닥에 둔다.
        # 역으로 보면 덱 맨앞이 초기 맨 뒤에서 두번째에 있는 셈.
        initialCard.insert(1, myDeque.popleft())
    elif skill == 3:
        # 3. 제일 밑에 있는 카드를 바닥에 둔다. 카드 2장 이상일때만 가능.
        # 역으로 보면 덱 맨앞이 초기 맨 앞에 있는 셈.
        initialCard.append(myDeque.popleft())

print(*initialCard) # 오 씨바 이런방법이 https://hwiyong.tistory.com/193