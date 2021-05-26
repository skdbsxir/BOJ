"""
나이와 이름이 순서대로 주어짐.
나이가 적은 순으로 정렬해서 출력
나이가 같으면 먼저 기입된 것 부터 출력.

3
21 Junkyu
21 Dohyun
20 Sunyoung

20 Sunyoung
21 Junkyu
21 Dohyun
"""
"""
myDict = {}

N = int(input())

# 근데 딕셔너리는 중복을 허용하지 않는데...
for i in range(N) :
    key, value = input().split()
    myDict[key] = value
    # key가 이미 myDict에 있으면, key에 해당하는 value에 리스트로 append?
    if key in myDict :
        myDict[key] = [myDict[key], value]
    
    
print(myDict)
"""

# 이거 틀리대 ㅠㅠㅠ 
# 맞았다!
from collections import defaultdict # 중복허용해서 넣기

N = int(input())
myDict = defaultdict(list)

for i in range(N):
    key, value = input().split()
    key = int(key) # 입력받은 key가 str. int로 바꾸면 된다~
    myDict[key].append(value)

# print(myDict)
# key가 현재 string으로 들어왔다. 이걸 int형으로 못바꿀까

# Dict 내용을 key기준 정렬해서 출력?
print('\n\n')
for key, value in sorted(myDict.items()) :
    # print(key)
    for list_item in value :
        print(key, list_item)
