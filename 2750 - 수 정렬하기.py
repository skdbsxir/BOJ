import sys

N = int(input())

myList = []
for i in range(N) :
    myInput = list(map(int, input().split()))
    myList.append(myInput[0])
    
if len(myList) != N :
    sys.exit(0)

#print(myList)    
# 5 2 3 4 1
for i in range(len(myList)) :
    for j in range(len(myList)) :
        if myList[i] < myList[j] :
            myList[i], myList[j] = myList[j], myList[i]

for i in range(len(myList)) :
    print(myList[i], end='\n')
    