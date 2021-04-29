myText = []
myVowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
while True :
    vowelCount = 0
    myText = input()
    if myText == '#' :
        break
    # myText.append(line)
    for i in myText:
        if i in myVowel :
            vowelCount += 1
    print(vowelCount)
"""
myVowel = 'aeiouAEIOU' 
vowelCount = 0
print(myText)
for i in myText :
    print(i)
    if i in myVowel :
        vowelCount += 1
    print(vowelCount)
"""