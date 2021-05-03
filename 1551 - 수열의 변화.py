import sys

# N, K 입력
N, K = map(int, input().split())

# 예외처리
if N > 20 or N < 0 :
    sys.exit(0)
elif K < 0 or K > N-1 :
    sys.exit(0)

# 리스트 입력    
myList = list(map(int, input().split(',')))
# print(len(myList))

counter = 0
"""
while counter != K:
    for i in range(N-1):
        #newList[i] = myList[i+1] - myList[i]
        #print(i)
        newList.append((myList[i+1]-myList[i]))
    counter += 1
""" 
if K == 0:
    print(*myList, sep=',')
    
else :
    while counter != K :
        newList = []
        for i in range(len(myList)-1):
            #newList.append((myList[i+1] - myList[i]))
            newList.insert(i, myList[i+1] - myList[i])
            #print(newList)
        # 새 리스트 선언할 필요 없이, 기존 리스트에 결과물을 넣으면 되는 것...
        myList = newList[:]
        counter += 1
    print(*myList, sep=',')
    
"""
def minusFunc(myList) :
    newList = []   
    for i in range(N-1):
        newList.insert(i, myList[i+1] - myList[i])
    return newList

if K == 0:
    newList = myList[:]
elif K == 1:
    minusFunc(myList)
else:
    minusFunc(myList)
    newList2 = []
    while counter != K:
"""  