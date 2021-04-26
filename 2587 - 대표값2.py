import sys

# Lambda 함수 이용. 일정 크기만큼 입력.
# 이걸 한 줄로 줄일순 없을까.
myList = list(input() for _ in range(5))
myList = list(map(int, myList))
# print(myList)

# 주어지는 자연수는 100보다 작은 10의 배수
for i in range(0, len(myList)):
    if myList[i] >= 100 :
        sys.exit(0)
    elif (myList[i] % 10) != 0 :
        sys.exit(0)

# 평균 계산
def calcMean(myList) :
    a = 0
    for i in range(len(myList)) :
        a += myList[i]
    return int(a / 5)

# 중앙값 계산
def calcMedi(myList) :
    # sortedList = myList.sort() 하면 왜 None 이 나오는걸까.
    sortedList = sorted(myList)
    return sortedList[2]
        
print(calcMean(myList), calcMedi(myList))

