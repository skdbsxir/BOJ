"""
스페이스로 구분된 단어들 리스트가 입력. 이를 반대 순서로 출력.
this is a test -> test a is this
foobar -> foobar
all your base -> base your all
"""
# import sys
# Test Case 수
N = int(input())
# N = sys.stdin.readline()
"""
wordList = list(map(str, input().split()))
# print(wordList)

# wordList 원소를 순서대로 스택에 push, 위에서부터 pop.
myStack = []

for i in range(len(wordList)):
    myStack.append(wordList[i])

revList = []
for i in range(len(myStack)) :
    # print('Case #',i,': ', myStack.pop(), end=' ')
    revList.append(myStack.pop())
    
for i in range(len(revList)) :
    # print('Case #',i,': ', revList[i], end=' ')
"""         
def reverseWord(sampList):
    # 이미 리스트에 순서대로 들어갔으니 빼기만 하면 되지 않을까
    revList = []
    for i in range(len(sampList)):
        revList.append(sampList.pop())
    
    # revList엔 들어올거 들어왔지
    return revList

for i in range(N):
    wordList = list(map(str, input().split()))
    # wordList = list(map(str, sys.stdin.readlines().split()))
    print('Case #%d:'%(i+1), ' '.join(reverseWord(wordList)))