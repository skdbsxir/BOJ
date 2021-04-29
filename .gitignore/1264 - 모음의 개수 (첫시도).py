"""
1. 스택을 만들고 - 한 스택마다 입력받고 push - 반복문 후 스택 안에서 find?
2. 리스트에 차례로 입력 - how?
"""
import sys
"""
myText = []
while input() != '#' :
    myInput = input()
    if myInput :
        myText.append(myInput)
    else:
        break
myTextt = '\n'.join(myText)
print(myTextt)
"""
"""
myText = []
while input() != '#':
    myIn = input()
    if myIn :
        myText.append(myIn)
    print('내입력 : ', myIn)
    print('\n들어갈거 : ', myText)
"""
myText = []
while True :
    line = input()
    if line == '#' :
        break
    else :
        myText.append(line)
"""       
for i in myText:
    print(i)
"""
# print(myText)

"""
입력받은 myText 리스트에서 이제 모음을 찾자.
 > i번째 리스트엔 i번째에 입력한 문장 전체가 들어감.
 > for문. 범위는 i in range myText 가 되나? 맞다.
 > 플래그 변수를 하나 지정. 리스트 index로 활용.
 > 각 인덱스마다 모음을 찾자. - How?
  >> 모음을 저장한 리스트 생성
  >> for i in 입력한텍스트
  >> if '모음을 저장한 리스트의 개별요소' in '입력한 텍스트'
  >> count++
""" 
"""
number = 0   
for i in myText:
    print(myText[number])
    number = number + 1
"""
indexNumber = 0
vowelCount = 0
myVowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# myVowel = 'aeiouAEIOU' 

"""
for i in myText :
    aCount = myText[i].count('a')
    eCount = myText[i].count('e')
    iCount = myText[i].count('i')
    oCount = myText[i].count('o')
    uCount = myText[i].count('u')
    vowelCount = aCount + eCount + iCount + oCount + uCount
    indexNumber += 1
    print(vowelCount)
"""
for i in myText :
    print(i)
    if i in myVowel :
        vowelCount += 1
    print(vowelCount)

# 아앙ㄱ 오애왜애애앵 
