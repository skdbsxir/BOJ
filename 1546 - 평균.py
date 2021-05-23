"""
점수 중 최대값 M
모든 점수를  (점수/M)*100 으로 바꿈.

이렇게 바꾼 점수로 평균 계산.
"""
N = int(input())
scoreList = list(map(int, input().split()))

# 1. 최대값을 찾는다
maxVal = max(scoreList)
#print(maxVal)

# 2. 모든 점수를 (점수 / 최대값) * 100 으로 바꾼다.
# 40 80 60 -> 50 100 75
# 3 10 -> 30 100
newList = []
for i in range(len(scoreList)) :
    newList.append((scoreList[i] / maxVal) * 100)

#print(newList)

# 3. 새로운 평균을 계산.
print(sum(newList) / N)