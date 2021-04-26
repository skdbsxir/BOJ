import sys

# N : 수열 크기 // X : 비교 숫자
N, X = map(int, input().split())

# 허용범위 넘으면 에러.
if N < 1 :
    sys.exit(0)
    
if X > 10000 :
    sys.exit(0)
    
# 수열 A를 이루는 정수 N개.
myList = list(map(int, input().split()))

# 수열 A 크기가 N보다 크면 에러.
if len(myList) > N :
    sys.exit(0)

# index 범위는 myList[0] ~ myList[N==myList길이].     
for i in range(0, len(myList)) :
    if myList[i] < X :
        print(myList[i])