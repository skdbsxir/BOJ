"""
새로운 Queue.

1. 현재 Queue의 가장 앞에 있는 문서의 중요도 확인
2. 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 있다면
    이 문서를 인쇄하지 않고 Queue의 가장 뒤에 재배치.
    그렇지 않으면 바로 인쇄.
    
A, B, C, D가 있고 중요도가 2, 1, 4, 3이라면
    C 인쇄 --> B D A (1 3 2)
    D 인쇄 --> A B (2 1)
    A 인쇄 --> B (1)
    B 인쇄 --> 끝
    
문서 수와 중요도가 주어졌을 때, 어떤 문서가 몇번째로 인쇄되는지?
위 예에서 C는 1번째, A는 3번째로 나옴.

입력: 첫줄은 테스트 케이스. 각 케이스는 두줄로 구성.
    케이스 첫줄엔 문서수 N, 몇번째로 인쇄되는지 궁금한 문서가 
    현재 Queue에서 몇번째에 놓여있는지 나타내는 정수 M. ㅇ
    케이스 두번째줄엔 N개 문서의 중요도가 순서대로.
    중요도가 같은 문서는 여러개 있을 수 있음.
    
3

1 0
5           --> 1

4 2
1 2 3 4     --> 2

6 0
1 1 9 1 1   --> 5
"""
# 덱 쓰자.
from collections import deque

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    myQueue = deque(map(int, input().split()))
    
    # 각 큐에 해당하는 index도 만들어서 비교?
    index = deque(list(range(N))) # 문서수 N 만큼.
    counter = 0
    
    # Queue 비울때 까지
    while len(myQueue) != 0:
        # 맨앞이 최대
        if myQueue[0] == max(myQueue):
            counter += 1
            myQueue.popleft()
            if index.popleft() == M:
                print(counter)
        # 뒤에 더 큰게 있으면 맨뒤로.
        else:
            myQueue.append(myQueue.popleft())
            index.append(index.popleft())