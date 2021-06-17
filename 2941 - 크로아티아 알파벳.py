"""
c= c- dz= d- lj nj s= z= 는 크로아티아 알파벳
총 몇개의 크로아티아 알파벳이 있는지?
"""

# 얼마 안되니 미리 선언해두자.
croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 입력받아 한개씩 count?
myWord = input()
counter = 0

for i in range(len(croatian)) :
    # 문자가 입력받은거에 있으면
    if croatian[i] in myWord :
        # 그 갯수 세고 문자는 임의로 바꿈 counter에 저장
        wordCount = myWord.count(croatian[i])
        myWord = myWord.replace(croatian[i], '*')
        # print(myWord)
        counter += wordCount
        # print(counter)

# ljes=njak
    # lj s= nj : 3개의 특수 알파벳 
    # e a k : 3개의 알파벳
        
# *이었던걸 그냥 다시 붙여주면 될듯
myWord = myWord.replace('*', '')
# print(myWord)
counter += len(myWord)
print(counter)
        