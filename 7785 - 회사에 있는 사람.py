"""
로그가 주어졌을 때 회사에 있는 모든 사람 구하기

첫줄엔 출입기록수 n
둘째줄엔 이름 + enter || leave.

출력은 회사에 있는 사람의 이름을 사전 역순으로 한줄에 한명씩 출력.
"""
import sys
# N = int(input())
N = int(sys.stdin.readline())
"""
myList = []
for i in range(N):
    myList.append(input().split())
    
# 앟 이거 뭐 어케 할수있을거같은데
for name, state in myList:
    if state == 'leave':
        myList.remove(name)
""" 
# 그냥 딕셔너리 씁시다...      
myDict = {}
for i in range(N):
    # name, log = input().split()
    name, log = sys.stdin.readline.split()
    # enter면 넣고, 아니면 지우고
    if log == 'enter':
        myDict[name] = 1
    else:
        del myDict[name]
        
#print(myDict)

# Key만 뽑아서 역순정렬, 출력.
print('\n'.join(sorted(myDict.keys(), reverse=True)))
# sys.stdin 쓰는데 왜 런타임에러 AttributeError 뜨지 