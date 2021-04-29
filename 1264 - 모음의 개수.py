myText = [] # 입력받은 텍스트를 저장할 리스트 선언.
myVowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] # 모음 리스트.

while True :
    vowelCount = 0
    myText = input()
    
    # '#'입력하면 끝.
    if myText == '#' :
        break
    
    for i in myText:
        if i in myVowel :
            vowelCount += 1
    print(vowelCount)