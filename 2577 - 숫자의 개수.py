"""
3개의 자연수 A,B,C 계산. 결과에서 0~9의 숫자가 몇번 쓰였는지 출력.
출력은 순서대로 0부터 9까지 각각 몇번 쓰였는지.

150
266
427

"""

A = int(input())
B = int(input())
C = int(input())

result = str(A * B * C)

# 결과를 str으로 받고, 이를 딕셔너리 형태로 저장하면 될듯?
resList = []
resDict = {}
for i in range(len(result)) :
    # print(result[i])
    resList.append(result[i])

for i in set(resList):
    resDict[i] = 0
    
for i in resList :
    resDict[i] = resDict[i] + 1
    
# print(resDict) # {'3': 2, '1': 1, '7': 2, '0': 3}
    
# for문, 딕셔너리, 해당원소를 key로 해서 출현값을 출력, 없으면 0.
    # 0~9까지 범위에서
    # resDict의 key가 있는지? 있으면 value를 출력, 없으면 0.
        ## range(9)는 왜 범위 숫자를 생성못하지? numpy는 못쓰는데
        ## 0~9까지 {'숫자' : 0}을 저장한 딕셔너리를 먼저 선언? 
# print(resDict[key]) = value

"""
for key, value in sorted(resDict.items()) :
    if str(resDict.keys()) in str(range(0, 9)) :
        print(value)
    else:
        print('0')
"""
"""
for i in str(list(range(9))) :
    print(resDict.get(i))
"""
"""
numbers = list(range(10))
for i in str(numbers) :
    print(resDict.get(i))
"""
# 그냥 딕셔너리 새로 하나만들자.
numberDict = {
        '0':0,
        '1':0,
        '2':0,
        '3':0,
        '4':0,
        '5':0,
        '6':0,
        '7':0,
        '8':0,
        '9':0
        }
for i in numberDict :
   #  print(resDict.get(i)) # None이 나오는걸 어떻게할까. ㅇㅋ.
    if resDict.get(i) == None :
        print('0')
    else:
        print(resDict.get(i))
