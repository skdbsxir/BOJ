"""
8개의 문제
총 점수는 가장높은 점수 5개의합

입력 : 한줄씩 걸쳐 총 8개의 점수. 0이상 150이하. 
        (각 문제는 1번, 2번, ... , 8번)
출력 : 첫줄엔 참가자의 총점 출력. (가장 높은 점수 5개의 합)
        둘째줄엔 어떤 문제가 최종점수에 포함되는지 공백으로 구분.
        문제 번호가 증가하는 순서로.
"""
myList = []
for _ in range(8):
    myList.append(int(input()))
    
# print(myList)

# 정렬하고 맨앞 5개가 총점수에 들어가는 점수.
sortList = sorted(myList, reverse=True)
# print(sortList)

score = sum(sortList[:5])
print(score)

# 정렬한 상태에서 기존 index를 어떻게

# 두 리스트를 비교해서 index만을 받아온다?
# sortList의 맨앞 5개 값을 
# 기존 List에서 index만 꺼내오기?
"""
print(sortList[:5])
myIndex = []
for i in range(len(myList)):
    if sortList in myList:
        myIndex.append(myList.index(sortList[i]))

print(myIndex)
"""

indexList = []
for i in sortList:
    if i in myList:
        # print(myList.index(i))
        # indexList.append(sortList.index(i))
        # print(myList.index(sortList[:5]))
        indexList.append(myList.index(i) + 1) # 문제 번호는 index + 1
# print(indexList)

# 앞 5개가 점수에 들어가는 문제번호.
answer = indexList[:5]

for i in sorted(answer):
    print(i, end=' ')

"""
indexList = []
# 2중for문 돌리는게 맞나
for i in range(len(myList)):
    for j in range(len(myList)):
        if sortList[i] == myList[j] :
            indexList.append(j)
 """           
