"""
이름에서 b와 g의 갯수를 셈.
g가 더 많으면 좋은놈 GOOD
b가 더 많으면 나쁜놈 A BADDY
둘이 같거나 없으면 중립 NEUTRAL

출력은 입력문자열 + is + GOOD/A BADDY/NEUTRAL
"""
"""
n = int(input())
nameList = []

# 입력 자체를 lower해서 받자. 그러면 출력이 좀 거시기
for i in range(n) :
    # nameList.append(input().lower().split(' '))
    nameList.append(input().split(' '))
# print(nameList[0])
# print('\n')
"""
"""
for i in range(len(nameList)):
    for j in range(len(nameList)) :
        tempList.append(nameList[i][j].lower())
"""
"""
2

Algorithm Crunching Man

Green Lantern

--> [['Algorithm', 'Crunching', 'Man'], ['Green', 'Lantern']]
"""
"""
for i in range(len(nameList)) :
    bCount = 0
    gCount = 0
    for j in range(len(nameList[i])) :
        print('%d번째 입력값 내용물 : ' % (i), nameList[i][j])
        if 'b' in nameList[i][j].lower() :
            bCount += 1
        if 'g' in nameList[i][j].lower() :
            gCount += 1
 
    if gCount > bCount :
        print(' '.join(nameList[i]) + ' is GOOD')
    elif gCount < bCount:
        print(' '.join(nameList[i]) + ' is A BADDY')
    else :
        print(' '.join(nameList[i]) + ' is NEUTRAL')
"""
"""
for i in range(len(nameList)) :
    for j in range(len(nameList[i])) :
        if nameList[i][j].lower().count('g') > nameList[i][j].lower().count('b'):
            print(' '.join(nameList[i]) + ' is GOOD')
            pass
        elif nameList[i][j].lower().count('g') < nameList[i][j].lower().count('b'):
            print(' '.join(nameList[i]) + ' is A BADDY')
            pass
        else :
            print(' '.join(nameList[i]) + ' is NEUTRAL')
"""
# 같은 for문안에서 그냥 입력받고 비교하는게 맞을듯
# 아 split안쓰고 그냥 그대로 받으면...
n = int(input())
nameList = []
for i in range(n) :
    nameList.append(input())
# print(nameList)
for i in range(len(nameList)) :
    if nameList[i].lower().count('g') > nameList[i].lower().count('b'):
        print(''.join(nameList[i]) + ' is GOOD')
        continue
    elif nameList[i].lower().count('g') < nameList[i].lower().count('b'):
        print(''.join(nameList[i]) + ' is A BADDY')
        continue
    else :
        print(''.join(nameList[i]) + ' is NEUTRAL')