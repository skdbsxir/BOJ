"""
정수를 저장하는 deque.

double-ended queue. 양쪽 끝에서 삽입과 삭제가 모두 가능. 큐+스택 인 형태?

push_front X : 정수 X를 덱의 앞에 삽입.
push_back X : 정수 X를 덱의 뒤에 삽입.
pop_front : 덱 가장 앞 정수를 빼고, 그 수를 출력. 덱이 비어있으면 -1 출력.
pop_back : 덱 가장 뒤 정수를 빼고, 그 수를 출력. 덱이 비어있으면 -1 출력.
size : 들어있는 정수 개수 출력
empty : 비어있으면 1, 아니면 0
front : 가장 앞에 있는 정수 출력. 정수가 없으면 -1 출력.
back : 가장 뒤에 있는 정수 출력. 정수가 없으면 -1 출력.
"""
import sys

# 명령 수
# N = int(input())
N = int(sys.stdin.readline())

myDeque = []

def push_front(x) :
    # 앞에 삽입
    myDeque.insert(0, x)

def push_back(x) :
    # 뒤에 삽입
    myDeque.append(x)

def pop_front() :
    if not myDeque:
        return -1
    # 맨 앞 원소 제거
    # 0 th index를 remove? 이걸 어케하지
    # pop(0) Okay.
    else:
        return myDeque.pop(0)

def pop_back() :
    if not myDeque:
        return -1
    # 맨 뒤 원소 제거
    else:
        return myDeque.pop()

def size() :
    return len(myDeque)

def empty() :
    if len(myDeque) == 0:
        return 1
    else:
        return 0

def front():
    if not myDeque:
        return -1
    else:
        return myDeque[0]

def back():
    if not myDeque:
        return -1
    else:
        return myDeque[-1]

# N개의 입력에 따라 처리
for i in range(N):
    # command = input().split()
    command = sys.stdin.readline().rstrip().split()
    
    if command[0] == 'push_front':
        push_front(command[1])
    elif command[0] == 'push_back':
        push_back(command[1])
    elif command[0] == 'pop_front':
        print(pop_front())
    elif command[0] == 'pop_back':
        print(pop_back())
    elif command[0] == 'size':
        print(size())
    elif command[0] == 'empty':
        print(empty())
    elif command[0] == 'front':
        print(front())
    elif command[0] == 'back':
        print(back())