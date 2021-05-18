import sys

N = int(input())

myList = []
for i in range(N) :
    #myInput = sys.stdin.readlines()
    #myList.append(myInput[0])
    #myList = list(map(int, sys.stdin.readlines()))
    #myList.append(int(input()))
    myList.append(int(sys.stdin.readline()))

#print(myList)  
if len(myList) != N :
    sys.exit(0)
    
def merge(list1, list2) :
    newList = []
    while len(list1) > 0 or len(list2) > 0 :
        # 둘다 남음
        if len(list1) > 0 and len(list2) > 0 :
            # 우측이 크다면
            if list1[0] <= list2[0] :
                newList.append(list1[0])
                list1 = list1[1:]
            # 좌측이 크다면
            else :
                newList.append(list2[0])
                list2 = list2[1:]
        # 하나만 남음
        elif len(list1) > 0 :
            newList.append(list1[0])
            list1 = list1[1:]
        elif len(list2) > 0 :
            newList.append(list2[0])
            list2 = list2[1:]
    return newList
    
    
def mergeSort(x) :
    if len(x) <= 1 :
        return x
    
    # 중앙
    mid = len(x) // 2
    # 중앙 기준으로 쪼개고
    L1 = x[:mid]
    L2 = x[mid:]
    # 다시 재귀
    S1 = mergeSort(L1)
    S2 = mergeSort(L2)
    # 결과합치기
    return merge(S1, S2)
    
ansList = mergeSort(myList)

for i in ansList :
    print(i)    