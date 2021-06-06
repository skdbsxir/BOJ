"""
입력된 N개의 단어들을

길이가 짧은것 부터
길이가 같으면 사전순으로

정렬.
"""
N = int(input())

myList = []
for i in range(N):
    myList.append(input())
    
# print(myList)
# print(myList.sort(key = lambda x: len(x)))
noDupList = list(set(myList)) # 중복 제거
sortedList = sorted(noDupList) # 알파벳 순 정렬
# print(sortedList)

# 이거 시간초과난다.
"""
# 단어 길이순으로 정렬?
 ## 리스트 전체를 순회해서
 ## 문자열의 길이 순으로 정렬?
for i in range(len(sortedList)) :
    for j in range(len(sortedList)) :
        if len(sortedList[i]) < len(sortedList[j]) :
            sortedList[i], sortedList[j] = sortedList[j], sortedList[i]
"""
# sortedList = sorted(myList)
# print(sortedList)

# 결과 리스트에 sortedList 각 원소의 길이 and 원소를 저장.
resultList = []
for i in sortedList:
    resultList.append((len(i), i))

# 정렬.
resultList.sort()

# 중복되는 단어는 제외.
# resultList = list(set(sortedList))
# [resultList.append(x) for x in sortedList if x not in resultList]

for i, j in resultList:
    print(j)
