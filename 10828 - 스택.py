"""
정수를 저장하는 stack.

push X : 정수 X를 stack에 삽입.
pop : stack 가장 위 정수를 빼고, 그 수를 출력. stack이 비어있으면 -1 출력.
size : 정수 개수 출력
empty : 비어있으면 1, 아니면 0
top : 가장 위에 있는 정수 출력. 정수가 없으면 -1 출력.
"""
# 제출용을 위해 import sys. (시간때문에...)
import sys

# 명령 수
# N = int(input())
N = int(sys.stdin.readline())

# stack 미리 선언
myStack = []

# 구현해야할 함수가 위의 5개.

def push(x) :
    myStack.append(x)  

def pop():
    if not myStack:
        return -1
    else:
        return myStack.pop()

def size() :
    return len(myStack)

def empty() :
    if len(myStack) == 0:
        return 1
    else:
        return 0

def top():
    if len(myStack) == 0:
        return -1
    else :
        return myStack[-1]

# N개의 명령에 따라 처리
for i in range(N):
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
    elif command[0] == 'top':
        print(top())
    