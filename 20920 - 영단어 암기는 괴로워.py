"""
영어 단어장은 다음의 우선순위를 차례로 적용해 만든다.

1. 자주 나오는 단어일수록 앞에 배치
2. 해당 단어의 길이가 길수록 앞에 배치
3. 알파벳 사전순으로 앞에 있는 단어일수록 앞에 배치

길이가 M 이상인 단어들만 외운다.

입력 : 지문에 나온 단어의 개수 N, 단어의 길이 M
      둘째 줄 부터 N+1 줄 까지 외울 단어를 입력. 소문자로만 주어지고, 단어 길이는 10을 안넘는다.
      단어가 반드시 1개 이상 존재하는 입력만 주어진다. 중복단어 입력이 된다는 소린가.
"""

import sys
N, M = map(int, input().split())

wordList = []
for _ in range(N):
    wordList.append(input())
    # wordList.append(sys.stdin.readline().rstrip())
    
# print(*wordList)

# 입력받은걸 일단 Dict형태로 저장?
wordDict = {}
for i in wordList:
    try:
        wordDict[i] += 1
    except:
        wordDict[i] = 1
print('\n')
print(wordDict)
print('\n')
print(wordDict.items())
print('\n')
#print(wordDict.keys())       

# 딕셔너리 안에서 len(key) >= M인 것들만 뽑는다. 이어서
#  1. value가 가장 높은걸 먼저 뽑고
#  2. len(key)가 가장 긴걸 그 다음으로 뽑고
#  3. sort해서 나오는걸 뽑는다.


# 먼저 len(key) >= M 인것부터 뽑자.
# 리스트가 아니라 Dict.items를 그대로 넘겨주진 못하나? 되네.
# wordList2 = []
wordDict2 = {}
for word, appearance in wordDict.items():
    if len(word) >= M:
        # wordList2.append(word)
        wordDict2[word] = [appearance, len(word)]

print(wordDict2)
print('\n')

# value 순으로 정렬해두자.
sortDict = sorted(wordDict2.items(), key=lambda x: x[1], reverse=True)
print(sortDict) # 반환이 리스트로 되는구나.
print('\n')
# 이렇게 하면 key순으로 정렬은 안됐다. 
# append 1, attendance 1 인데 ap가 at보다 사전 앞이라서 append가 먼저 옴.
# 단어 길이를 딕셔너리에 같이 저장할수 있나? wordDict2[word] = [appearance, len(word)]?
# 됐네. 이렇게하니까 그냥 됐는데?

# 여기서 이제 key만 뽑아오자.
ansList = []
for i in range(len(sortDict)):
    ansList.append(sortDict[i][0]) # 리스트 안 요소의 첫번째 것만 빼오자.

for i in range(len(ansList)):
    print(ansList[i], end='\n')

"""
# 위 풀이 틀렸답니다. 시간초과도 아니고... 열받네
N, M = map(int, input().split())
wordList = []
for _ in range(N):
    wordList.append(input())

wordDict = {}
for i in wordList:
    try:
        wordDict[i] += 1
    except:
        wordDict[i] = 1

wordDict2 = {}
for word, appearance in wordDict.items():
    if len(word) >= M:
        # wordList2.append(word)
        wordDict2[word] = [appearance, len(word)]

sortDict = sorted(wordDict2.items(), key=lambda x: x[1], reverse=True)

ansList = []
for i in range(len(sortDict)):
    ansList.append(sortDict[i][0]) # 리스트 안 요소의 첫번째 것만 빼오자.

for i in range(len(ansList)):
    print(ansList[i], end='\n')
"""







