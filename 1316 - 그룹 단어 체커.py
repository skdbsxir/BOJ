"""
그룹단어 : 각 문자가 연속해서 다타나는 경우.
ccazzzzbb - 모두 연속해서 나옴.
kin - 모두 연속해서 한번씩 나옴.
aabbbccb - b가 한번 떨어져서 나오므로 그룹단어 X.
"""
"""
N = int(input())
myList = []
for i in range(N) :
    myList.append(input())
"""
# 단어를 쭉 둘러본다.
# 문자가 한번씩 나오면 OK.
# 문자가 연달아 나오는지 확인.
    # 그 뒤로 연달아 나온 문자가 또 나오면 그룹단어 X.
"""
string = 'aaaaaa'

counter = 0
isGroup = ''
for i in range(len(string)) :
    # 처음부터 끝까지 비교
    print('%d 번째 I loop' % i)
    for j in range(i+1, len(string)) :
        # 현재 단어랑 다음꺼랑 비교
        print('J loop - 비교대상 : %s and %s' % (string[i], string[j]))
        if string[i] == string[j] :
            counter += 1
            # 그 사이에 다른 단어가 껴있었다면?
            # 바로 이전것만 확인하면 되지 않을까?
            isGroup = 'Yes'
            if string[j] != string[j-1] :
                print('먼저꺼랑 확인 : %s 와 %s' % (string[j], string[j-1]))
                isGroup = 'No'
                print('J loop - 다른겁니다. %s' % isGroup)
                break 
            for k in range(j+1, len(string)) :
                # 같은 단어가 나왔고, 그 단어 뒤를 더 확인.
                # 여기서 걸렸구나.
                print('K loop - 비교대상 : %s and %s' % (string[j], string[k]))
                if string[i] == string[k] and string[j] != string[k]:
                    isGroup = 'No'
                    print('K loop - 다른겁니다. %s' % isGroup)
                    break
            if isGroup == 'No' :
                print('K loop 빠져나갈게요')
                break
        if isGroup == 'No' :
            print('J loop 빠져나갈게요')
            break
    if isGroup == 'No' :
        print('I loop 빠져나갈게요')
        break
            
if counter == 0:
    isGroup = 'Yes'
            
print(counter)
print(isGroup)
"""
# counter가 0이면 얘는 그룹단어.
# counter가 1 이상이면
    # counter가 +1된 위치 기준으로
    # 그 뒤로 다시 확인,
    # 같은 단어가 나오면 그룹단어가 X.
# happy 같이 붙어있는 경우는 counter + 1이 되면서 OK.
# abcabc 같이 떨어져있는 경우는 counter +1이 되는데 a와 a사이에 다른게 있음.

N = int(input())
myList = []
for i in range(N) :
    myList.append(input())
    
def wordChecker(string) :
    counter = 0
    isGroup = ''
    for i in range(len(string)):
        for j in range(i+1, len(string)):
            if string[i] == string[j] :
                counter += 1
                isGroup = 'Yes'
                if string[j] != string[j-1] :
                    isGroup = 'No'
                    break
                for k in range(j+1, len(string)):
                    if string[i] == string[k] and string[j] != string[k]:
                        isGroup = 'No'
                        break
                if isGroup == 'No' :
                    break
            if isGroup == 'No' :
                break
        if isGroup == 'No':
            break
        
    if counter == 0:
        isGroup = 'Yes'
    
    return isGroup

resList = []

for i in range(len(myList)) :
    resList.append(wordChecker(myList[i]))
    
print(resList.count('Yes'))

"""
반례하나 나옴
5

aba

ababba

abcca

aabc

a
4
이건해결

--------
1

aaaaaa
0
"""

"""
풀고나서 본 다른사람들의 풀이
https://aisiunme.github.io/algorithm/2018/08/13/baekjoon-group-word-checker-1316.md/
https://sw-beta.tistory.com/80
https://namhandong.tistory.com/67

find 함수......
"""