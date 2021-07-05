"""
D-쌍 : 거리가 D인 두 문자를 순서대로 나열한것.
ex. ZGBG에 대해
    0-쌍 (두 문자 사이 거리가 0): ZG, GB, BG
    1-쌍 (두 문자 사이 거리가 1): ZB, GG
    2-쌍 (두 문자 사이 거리가 2): ZG
이렇게 정의되는 모든 D-쌍들이 서로 다르면, 이 문자를 D-유일 하다고 함.

ex. AAA에 대해
    0-쌍 : AA, AA
    1-쌍 : AA
이므로, 0-유일하지 않으며 1-유일 하다.

모든 D에 대해 D-유일 하면, 이 문자열을 '놀라운 문자열'이라고 함.

입력 : 알파벳 대문자로만 구성된 문자열
출력 : 이 문자열이 놀라운 문자열인지 아닌지 출력
    ZGBG is surprising
    EE is surprising
    AABB is NOT surprising
"""
"""
word = list(input())
print(word)
print(set(word))
# D쌍을 다 구해서
# D쌍 중에 같은게 있으면 not surprising.

# 길이가1 or 길이가 2, set길이가 1이면 surprising.
if (len(word) == 1) or (len(word)==2 and len(set(word))==1):
    print(word[::], ' is surprising') # 나중에 고치자.
    

# 0만큼 떨어져있고, 1만큼 떨어져있고, 2만큼 떨어져있고...
# 0쌍 : 12 23 34 45 56
# 1쌍 : 13 24 35 46
# 2쌍 : 14 25 36
# print(word[0:len(word):2]) # slicing + stride

# 2중 for문밖에 생각이 안나는데
for i in range(len(word)):
    for j in range(len(word)):
        if word[i] + word[j] == word[i+1] + word[j+1]:
            print('no')
"""
while True:
    word = input()
    if word == '*':
        break
    flag = True
    
    # 이거 생각못한건 사고력 문젠듯.
    # 거리 0으로 하면 자기자신이랑 비교함.
    # range범위는 0이 아닌 1부터 하는게 맞다.
    # i : 뛰어넘을 칸 // j : 문자 위치
    for i in range(1, len(word)):
        myList = []
        for j in range(len(word)-i):
            print('현재 인덱스는 %d, %d' % (i, j))
            print('## 추가할 단어는 %s, %s' % (word[j], word[j+i]))
            myList.append(word[j] + word[j+i])
            print('** 현재 생성된 리스트는 ', myList)
        # 안에 중복되는 단어가 있는지?
        for k in range(len(myList) - 1):
            print('### 비교할 단어는 : ', myList[k], myList[k+1:])
            if myList[k] in myList[k+1:]:
                print('! 같은 단어가 있어요 : ', myList[k], myList[k+1:])
                flag = False
    
    if flag :
        print('{0} is surprising.'.format(word))
    else:
        print('{0} is NOT surprising.'.format(word))
        