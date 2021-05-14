import sys

# A : 낮에 올라가는 길이
# B : 밤에 떨어지는 길이
# V : 나무 길이
A, B, V = map(int, input().split())

if B > A :
    sys.exit(0)
elif A > V :
    sys.exit(0)
elif V > 1000000000 :
    sys.exit(0)

# 1 day 총 이동량 : A - B
# 2 day 총 이동량 : 1day + (A - B)
# 3 day 총 이동량 : 2day + (A - B)
# ...
# n day 총 이동량 : n-1 day + (A - B)
# if n day 총 이동량 == V : 종료 --> while문
"""
movement, day = 0, 0
while True :
    movement += (A - B)
    day += 1
    if movement >= V :
        print(day)
        break
""" 
"""
ex1) 2 1 5
mov1 = 2 - 1 = 1, day = 1
mov2 = 1 + (2 - 1) = 2, day = 2
mov3 = 2 + (2 - 1) = 3, day = 3
mov4 = 3 + (2 - 1) = 4, day = 4
mov5 = 4 + (2 - 1) = 5, day = 5 ??

ex2) 5 1 6
mov1 = 5 - 1 = 4, day = 1
mov2 = 4 + (5 - 1) = 8, day = 2
"""
# mov(n) = mov(n-1) + (A-B)
movement = A - B
movlist = [movement] # 첫날 움직임
#day = 0
"""
while True :
    movlist.append(movement)
    day += 1
    if sum(movlist) >= V :
        print(day)
        break
"""
def snailMovement(daytime, night, length) :
    movement = daytime - night
    moveList = list.append(movement)
    day = 1
    
    if movement == V :
        return print(day)
    else :
        """
    for i in range(1, length) :
        moveList.append((moveList[i-1] + movement))
        print(moveList)
        day += 1
        if moveList[-1] >= V :
            break
        """
    for i in range(1, length+1) :
        moveList[i] = snailMovement(daytime) # ㅁㄴㅇㄹㄴ으아앙 
    #return print(day)

snailMovement(A, B, V)
