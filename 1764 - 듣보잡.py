"""
듣도 못한 사람의 명단 N개
보도 못한 사람의 명단 M개

둘다 중복되는 듣도보도못한 사람의 명단 출력.

입력 : 듣도못한사람 수 N, 보도못한사람 수 M
        둘째 줄 부터 N줄에 걸쳐 듣도 못한 사람의 이름
        N+2째 줄 부터 보도 못한 사람의 이름 (N이후라고 하면 안되나)
출력 : 듣보잡의 수, 명단을 사전순 출력.
"""
N, M = map(int, input().split())

# nolookList = []
# nolistenList = []

# 아예 N+M길이만큼 입력받는게 나을듯
personList = []
"""
for _ in range(N):
    nolookList.append(input())
for _ in range(M):
    nolistenList.append(input())
"""
for _ in range(N+M):
    personList.append(input())

# print(N, M)
# print(nolookList)
# print(nolistenList)
# print(personList)

# 두 리스트에서 중복되는 사람이 듣보잡.
    # 리스트를 합쳐서 딕셔너리 형태로?
personDict = {}
# personList = nolookList + nolistenList
for i in personList:
    try:
        personDict[i] += 1
    except:
        personDict[i] = 1

# print(personDict)

# personDict에서 value >= 2 인 사람들이 듣보잡. 얘네만 빼자.
unknownPerson = []
for name, count in personDict.items():
    if count >= 2:
        unknownPerson.append(name)
        
# print(unknownPerson)

# 정렬해두고
unknownPerson.sort()

# print(unknownPerson)
# 사람 수, 사람 이름 출력
print(len(unknownPerson))
for i in range(len(unknownPerson)):
    print(unknownPerson[i])

"""
set을 쓰는 방법도 있네?

totalList = list(set(nolookList) & set(nolistenList))

"""
"""
nolookList = []
nolistenList = []
for _ in range(N):
    nolookList.append(input())
for _ in range(M):
    nolistenList.append(input())

totalList = list(set(nolookList) & set(nolistenList))
print(totalList) # 와 시발 ㅋㅋㅋㅋㅋㅋㅋㅋㅋ
"""