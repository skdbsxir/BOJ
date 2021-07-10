"""
N개의 원소를 가진 양방향 순환 큐. 연산 3가지.

1. 첫번째 원소 추출. a1,...,ak가 a2,...,ak로 변함.
2. 왼쪽 한칸 이동. a1,...,ak가 a2,...,ak,a1으로 변환.
3. 오른쪽 한칸 이동. a1,...,ak가 ak,a1,...,ak-1로 변환.

처음 포함된 수 N이 주어지고, 뽑아내려는 원소 위치가 주어짐.
원소를 주어진 순서대로 뽑는데 드는 2,3번 연산의 최소값을 출력

입력 : 큐의크기 N, 뽑아내려 하는 수의 개수 M.
      뽑아내려 하는 수의 위치가 순서대로.
      
출력 : 문제의 정답.

ex) 10 3 // 1 2 3 --> 1번 연산만 3번 하면 되므로 0.
"""
from collections import deque

N, M = map(int, input().split())
popList = list(map(int, input().split()))
# print(popList)
myDeque = deque([i+1 for i in range(N)]) # 크기 N의 덱 생성

# 1번연산 함수
def popLeft(sampleDeque):
    # sampleDeque.popleft()
    return sampleDeque.popleft()

# 2번연산 함수
def moveLeft(sampleDeque):
    # sampleDeque.append(sampleDeque.popleft())
    sampleDeque.rotate(-1) # 맨 앞 원소를 맨 뒤로
    return sampleDeque
    
# 3번연산 함수
def moveRight(sampleDeque):
    # sampleDeque.extendleft(sampleDeque.pop())
    sampleDeque.rotate(1) # 맨 뒤 원소를 맨 앞으로
    return sampleDeque    

# print('1번연산 한번 수행, 덱에서 나온거 : ', popLeft(myDeque))
# print('1번연산 한번 수행 후 덱 상태 : ', myDeque)
# print('2번연산 한번 수행, 덱상태 : ', moveLeft(myDeque))
# print('3번연산 한번 수행, 덱상태 : ', moveRight(myDeque))

"""
반복문 돌려서
맨 왼쪽값 == popList 요소 값 이면 popLeft
아니면 moveRight, moveLeft 하자.
    - 이 최적은 어떻게 할까
    - 뽑고자 하는 값이 중앙보다 왼쪽, 오른쪽 어디에 있는지 판단해야할듯.
"""
counter = 0
for findNum in popList:
    while True:
        # 덱 맨앞이 찾는거면 중단
        if myDeque[0] == findNum:
            popLeft(myDeque)
            break
        # 찾는 수가 중앙보다 왼쪽, 오른쪽 어디있는지?
        else:
            # 왼쪽에 있으면 왼쪽으로 이동 (2번연산)
            if myDeque.index(findNum) <= len(myDeque)//2:
                moveLeft(myDeque)
                counter += 1
            # 아니면 오른쪽 (3번연산)
            else:
                moveRight(myDeque)
                counter += 1
                
print(counter)
        
