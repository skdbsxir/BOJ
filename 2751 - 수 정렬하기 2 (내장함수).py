# 내장 정렬함수 Tim Sort는 O(nlogn).

import sys

sys.setrecursionlimit(100000)

N = int(input())
myList = []


for i in range(N) :
    #myList.append(int(input()))
    myList.append(sys.stdin.readline())
    
if len(myList) != N:
    sys.exit(0)
    
for i in sorted(myList) :
    #print(i)
    sys.stdout.write(myList(i) + '\n')