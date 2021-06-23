"""
조씨와 백씨한테 류씨의 위치를 계산하라는 명령
조씨 좌표 x1, y1
백씨 좌표 x2, y2

조씨가 계산한 류씨와의 거리 r1
백씨가 계산한 류씨와의 거리 r2

이때 류씨가 있을 수 있는 좌표의 수 출력

입력 첫줄은 테스트 케이스 수 T
입력 둘째줄은 x1 y1 r1 x2 y2 r2 가 순서대로.

출력은 각 케이스마다 류씨가 있을 수 있는 위치.
    위치 개수가 무한대면 -1 출력.
    
0 0 13 40 0 37 -> 2 : 두 원이 만나는 지점이 두곳.
0 0 3 0 7 4 -> 1 : 두 원이 만나는 지점은 딱 한곳. 
1 1 1 1 1 5 -> 0 : 한 원이 다른 원 안에 있음. 원이 만나지 않는다?
위치 개수가 무한대? 두 원이 일치하는 경우 인가?
"""
import math

T = int(input())

# x1 y1 r1 x2 y2 r2가 한번에 들어오니까 음
# x1, y1, r1, x2, y2, r2 = map(int, input().split())

"""
# 주어진 x,y 좌표에서
# 반지름 r크기의 원을 그려서
# 두 원이 만나는지/안만나는지 판단?
 # 이건 어떻게 할까 흠
# x1 +- r1, x2 +- r2 // y1 +- r1, y2 +- r2
 # 하나라도 같은게 있으면 한점에서 만난다?
# x,y랑 r가지고 좌표놀음하면 상하좌우 어디서 만나는지 조건따지기가 좀

# x1 y1 r1 : A원 // x2 y2 r2 : B원
def findMarine():
    counter = 0
    # 두 원이 일치하는 경우 --> 위치가 무한대.
"""

def findMarine(sampList) :
    dist = math.sqrt((sampList[0]-sampList[3])**2 + (sampList[1]-sampList[4])**2) # 거리 정의
    print('두점사이 거리 : ', dist)
    # 거리가 0이고 반지름이 같다 --> 동심원. 위치는 무한대.
    if (dist == 0) and (sampList[2] == sampList[5]):
        print('동심원이에요')
        counter = -1
    # r1+r2==dist or |r1-r2|==dist --> 내접 or 외접
    elif (sampList[2] + sampList[5] == dist) or (abs(sampList[2] - sampList[5]) == dist):
        print('내접/외접해요')
        counter = 1
    # 원이 두점에서 만남
    elif (abs(sampList[2] - sampList[5]) < dist) and (sampList[2] + sampList[5] > dist):
        print('두점에서 만나요')
        counter = 2
    # 그 외의 경우
    else:
        print('아무것도 아니에요')
        counter = 0
    
    return counter

for i in range(T):
    myList = list(map(int, input().split()))
    # print(myList)
    # list index : 0(x1), 1(y1), 2(r1), 3(x2), 4(y2), 5(r2)
    print(findMarine(myList))
    