"""
하루동안 팔린 책의 제목이 입력, 가장 많이 팔린 책의 제목을 출력.
책은 알파벳 소문자로만 이뤄짐

가장 많이 팔린 책의 제목 출력. 여러개일 경우 사전순으로 가장 앞서는 제목 출력.
"""
N = int(input())
sellDict = {}
myList = []
for _ in range(N):
    myList.append(input())

# print(myList)

# 받은 list로 Dict만들기
for i in myList:
    try:
        sellDict[i] += 1
    except:
        sellDict[i] = 1
        
print(sellDict)

# key기준 정렬 이러면 리스트가 되어버리는뎅
# sortDict = sorted(sellDict.keys())

# 그 안에서 맨앞 최대값 가져오기. 이건 최대값 한개일때만.
# print(max(sellDict, key=sellDict.get))

# https://bio-info.tistory.com/40
# list comprehension 써서 여러개 일단 꺼내오자
topSell = [key for key, value in sellDict.items() if max(sellDict.values()) == value]
print(topSell)

# 이걸 정렬하고 맨 앞에거로 꺼내오자
topSell.sort()
print(topSell[0])