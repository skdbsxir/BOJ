"""
N장의 카드 중 3장을 고름.
3장의 합이 M을 넘지 않으면서 M과 최대한 가깝게.

첫째줄 : 카드수 N, 3장의 합 M
둘째줄 : 카드에 쓰여있는 수

5 21
5 6 7 8 9
21 (6 + 7 + 8)

10 500
93 181 245 214 315 36 185 138 216 295
497 (245 + 216 + 36)
"""
# import random
from itertools import combinations

N, M = map(int, input().split(' '))

cardList = list(map(int, input().split()))

"""
list안에서 임의로 3장을 선택?
이 값들의 합이 M과 같거나 최대한 가까운경우 반복 종료.

최대한 가깝게?? 이걸 어떻게하지 

ㅋㅋㅋ ex2같은경우 random쓰면 무지성뽑기한다.
"""
"""
total = 0
while True:
    sampleList = random.sample(cardList, 3)
    print(sampleList)
    total = sum(sampleList)
    
    if total == M:
        break

    elif total >= M-3 and total <= M :
        break


print(total)
"""
"""
cardList에서 한장씩 뽑아서 새 리스트에 저장?
random 말고는 생각이 안나는데

Greedy?
브루트포스 분류인데 진짜 3중for문 돌리나?
"""
"""
total = 0
for i in range(0, len(cardList)):
    for j in range(i+1, len(cardList)):
        for k in range(j+1, len(cardList)):
            total = cardList[i] + cardList[j] + cardList[k]
            if total <= M:
                # 음...
# print(total)
"""
"""
N개중에서 3개를 고르는 거니까 N_C_3. (조합)
계속 뽑으면서 M보다 같거나 작은 최대의 합을 찾는다?
"""
maxSum = 0
for i in combinations(cardList, 3):
    # print(i)
    tempSum = sum(i)
    if tempSum > maxSum and tempSum <= M :
        maxSum = tempSum

print(maxSum)


