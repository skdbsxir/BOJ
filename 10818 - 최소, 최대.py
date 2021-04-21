import sys

N = int(input())

# 허용 범위 수를 넘기면 종료.
if N > 1000000 :
    sys.exit(0)
elif N < 1 :
    sys.exit(0)

# 리스트에 들어가는건 정수.
myArray = list(map(int, input().split()))

# 입력한 수의 갯수가 N과 일치하지 않으면 종료.
if len(myArray) != N :
    print('Wrong length')
    sys.exit(0)
    
# print(myArray)

# 리스트에서 최소, 최대 비교
def maxValue(myArray) :
    temp = 0
    for i in myArray :
        if temp == 0 or i > temp :
            temp = i
    return temp

def minValue(myArray) :
    temp = 0
    for i in myArray :
        if temp == 0 or i < temp :
            temp = i
    return temp

print(minValue(myArray), maxValue(myArray))
