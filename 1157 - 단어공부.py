"""
단어를 찾는다 -> 단어 빈도수 찾기
입력받은 단어는 str type. 인덱스 참조를 통해 단어 위치를 볼 수 있음.
 > 인덱스를 참조하고
 > 각 인덱스 별로 출현하는 단어를 저장?
 > 거기서 중복되는 수를 count? > 딕셔너리를 사용해보자.
"""
myWord = input().lower()

wordList = []
wordDict = {}

for i in range(len(myWord)) :
    wordList.append(myWord[i])
    
for i in set(wordList) :
    wordDict[i] = 0
    
for i in wordList :
    wordDict[i] = wordDict[i] + 1
    
    
# 값이 제일 높은 키를 찾는다. how? List Comprehension.
#for i, (key, value) in enumerate(wordDict.items()) :
#    print(i, key, value)
#print(max(wordDict, key=wordDict.get))

maxVal = [key for key, value in wordDict.items() if max(wordDict.values()) == value]

if len(maxVal) >= 2 :
    print('?')
else :
    print(maxVal[0].upper())