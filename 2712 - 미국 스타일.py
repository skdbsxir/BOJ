"""
<무게>
1 kg <-> 2.2046 lb
0.4536 kg <-> 1.0000 lb
1 l <-> 0.2642 g
3.7854 l <-> 1.0000 g
"""
T = int(input())
# myList = list(map(str, input().split()))
# myList[0] = float(myList[0])
myList = []

# 입력받고 앞 숫자는 float로 변환
for i in range(T) :
    myList.append(input().split())
    # print(myList)
    myList[i][0] = float(myList[i][0])

"""
# for i in myList:
#    print(i, end=' ')
for i in range(len(myList)) :
    print(*myList[i], sep=' ')
"""

"""
1 kg = 2.2046 lb
1 lb = 0.4536 kg
1 l = 0.2642 g
1 g = 3.7854 l
"""
def UnitConversion(x) :
    # 리스트 안 두번째 문자로 구분.
    # [[1.0, 'kg'], [2.0, 'lb']]
    for i in range(len(x)) :
        # kg 이면
        if x[i][1] == 'kg' :
            x[i][0] = x[i][0] * 2.2046
            x[i][1] = 'lb'
        # lb 이면
        elif x[i][1] == 'lb':
            x[i][0] = x[i][0] * 0.4536
            x[i][1] = 'kg'
        # l 이면
        elif  x[i][1] == 'l' :
            x[i][0] = x[i][0] * 0.2642
            x[i][1] = 'g'
        # g 이면
        elif x[i][1] == 'g' :
            x[i][0] = x[i][0] * 3.7854
            x[i][1] = 'l'
    return x
    
myList = UnitConversion(myList)
for i in range(len(myList)) :
    # print(*myList[i], sep=' ')
    # print('%4f' % (myList[i][0]), sep=' ')
    print("{:.4f}".format(myList[i][0]) + ' ' + myList[i][1])