"""
정수를 저장하는 queue.

First In First Out. 대기열 큐.

push X : 정수 X를 큐에 삽입.
pop : stack 가장 앞 정수를 빼고, 그 수를 출력. 큐가 비어있으면 -1 출력.
size : 들어있는 정수 개수 출력
empty : 비어있으면 1, 아니면 0
front : 가장 앞에 있는 정수 출력. 정수가 없으면 -1 출력.
back : 가장 뒤에 있는 정수 출력. 정수가 없으면 -1 출력.
"""
import sys

# 명령 수
# N = int(input())
N = int(sys.stdin.readline())

myQueue = []

def push(x) :
    # 넣을때부터 첫번째 위치에 넣으면
    # 나올땐 제일 먼저 넣은게 나오게 되는 셈.
    myQueue.insert(0, x)
    
def pop():
    if not myQueue:
        return -1
    else:
        return myQueue.pop()
    
def size():
    return len(myQueue)

def empty():
    if len(myQueue) == 0:
        return 1
    else:
        return 0

def front():
    if not myQueue:
        return -1
    else:
        # 제일 앞에있는 원소는 list 맨 끝원소. (제일 먼저들어온 놈)
        return myQueue[-1]

def back():
    if not myQueue:
        return -1
    else:
        # 제일 끝에 있는 원소는 list 맨 첫원소. (제일 마지막에 들어온 놈)
        return myQueue[0]
    
# N개의 명령에 따라 처리
for i in range(N) :
    # command = input().split()
    command = sys.stdin.readline().rstrip().split()
    
    if command[0] == 'push':
        push(command[1])
    elif command[0] == 'pop':
        print(pop())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'front':
        print(front())
    elif command[0] == 'back':
        print(back())