"""
한번 입었던 옷들의 조합을 절대 다시 입지 않음.
오늘 '안경', '코트', '상의', '신발' 을 입었으면 
다음날 '바지'를 추가로 입거나 '안경'대신 '렌즈'를 껴야함.

의상들이 주어졌으면, 알몸이 아닌 상태로 몇일동안 밖에 돌아다닐 수 있을까

입력 : 첫줄은 테스트 케이스. 최대 100.
      각 케이스 첫째 줄에는 가진 의상 수 n (0이상 30이하)이 주어짐.
      다음 n개엔 의상 이름과 의상 종류가 공백으로 주어짐. 같은 종류의 의상은 하나만 착용가능.

출력 : 각 케이스에 대해 알몸이 아닌 상태로 의상을 입을 수 있는 경우 출력.

ex)
 
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face

--
5
3

-----
첫번째 테스트 케이스 : headgear - (hat, turban), eyewear - (sunglasses)
    hat, turban, sunglasses, hat-sunglasses, turban-sunglasses 이므로 총 5개.
    
두번째 테스트 케이스 : face - (mask, sunglasses, makeup)
    mask, sunglasses, makeup 이므로 총 3개.

"""

"""
testCase = int(input()) # 테스트 케이스 수

for i in range(testCase):
    wearable = int(input()) # 의상 갯수.
    clothes = []
    for _ in range(wearable):
        clothes.append(input().split())

# print(clothes)

# 받은 걸 Dictionary로? 
# key는 뭐로두지 headgear, face 이런거로 두는게 맞을듯.
# https://stackoverflow.com/questions/48705143/efficiency-2d-list-to-dictionary-in-python
clothDict = {}
for kind in clothes:
    try:
        clothDict[kind[1]].append(kind[0])
    except KeyError:
        clothDict[kind[1]] = [kind[0]]
        
print(clothDict) # key는 headgear 같은 의상 종류, value는 의상 이름.

# key에 따라서 value끼리 조합을 돌리면 될거같은데 음...
# 일단은 key에 있는 내용들 전부 한개씩 꺼내보고
# 다음으론 한쪽 key와 다른쪽 key의 value를 쌍 묶고
# 반복하다보면 경우의 수가 전부 나오는게 아닌가

# 각 key에 있는 value들에 대해 n = len(value)라고 둔다면
    # 1. key별로 n_C_1 을 먼저 싹 계산하고
    # 2.
    # 조합 식 안써도 될거같은데
#print(clothDict.values())
#print(list(clothDict.values()))
#result = list(combinations(clothDict.values(), 1))
#print(result)
#print(len(result))

print(clothDict.keys())

for key in clothDict.keys():
    print(clothDict[key]) # 이걸 단순히 곱해주면 되는거 아닌가? 

# 아무것도 안고르는 경우가 있구나 
# 아무것도 안입는 경우를 추가? 딕셔너리 다시짜자. 아니 그냥 공백을 추가해주면 되지않나
    clothDict = {}
    for kind in clothes:
        try:
            clothDict[kind[1]].append(kind[0])
        except :
            clothDict[kind[1]] = [kind[0], ''] # 이렇게하면 되지않을까

#print(clothDict)
#print(clothDict.values())

# 그럼 답은 value들을 그냥 곱한게 아닐까?
    ans = 1
    for key in clothDict.keys():
        ans *= len(clothDict[key])

# 왜 6, 4나오지
    # 아무것도 안입는 '' - '' 끼리 묶이는 게 있구나 빼주자.
    print(ans-1) 
"""    
# 이 씨이잇벌 빌어먹을 indent
testCase = int(input()) # 테스트 케이스 수

for i in range(testCase):
    wearable = int(input()) # 의상 갯수.
    clothes = []
    for _ in range(wearable):
        clothes.append(input().split())
    
    clothDict = {}
    for kind in clothes:
        try:
            clothDict[kind[1]].append(kind[0])
        except :
            clothDict[kind[1]] = [kind[0], '']
    ans = 1
    for key in clothDict.keys():
        ans *= len(clothDict[key])
    print(ans-1) 
