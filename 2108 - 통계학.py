"""
N은 홀수

N개의 수를 받아서 산술평균, 중앙값, 최빈값, 범위를 출력.
"""
# 모듈 쓰자...
import statistics
import sys
from collections import Counter

# 개같은 시간초과
N = int(sys.stdin.readline())
myList = []
for i in range(N):
    myList.append(int(sys.stdin.readline()))
    
# print(myList)

# 미리 정렬해두고 계산하면 편할듯.
myList.sort()

# print(myList)
"""
# 평균 (반올림 한 값)
mean = sum(myList) // len(myList)

# 중앙값 : 중앙에 위치하는 값
    # 리스트 전체길이 에서 가운데 위치한놈
median = myList[(len(myList)-1//2)]
print(median)
"""
mean = round(statistics.mean(myList))
median = statistics.median(myList)
"""
이거 또 에러날듯? 저번에도 try-except 꼼수 에러난거 보니.
try :
    mode = statistics.mode(myList)
except:
    mode = myList[1]
"""    
# Counter 쓰자.
myDict = Counter(myList)
myMode = myDict.most_common()
if len(myList) > 1:
    if myMode[0][1] == myMode[1][1] :
        mode = myMode[1][0]
    else :
        mode = myMode[0][0]
else :
    mode = myMode[0][0]
    
minmax = myList[-1] - myList[0] # 최대값 - 최소값

print(mean)
print(median)
print(mode) 
print(minmax)