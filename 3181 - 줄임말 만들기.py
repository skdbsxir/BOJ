passList = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
# [원소 위치][해당 원소의 단어 위치]
"""
# i를 써서 리스트 자체를 참조
for i in passList:
    print(i)
# i를 써서 리스트 인덱스로 참조
for i in range(len(passList)) :
    print(passList[i])
"""
    
myList = list(input().split())
#print(myList)

ans = []
"""
for i in myList :
    # 첫 글자를 대문자로 변환해 삽입
    ans.append(i[0].upper())
    
    # 만약 ans의 첫번째 대문자가 passList의 대문자와 같으면 유지
    # 그 외 위치에서의 대문자가 passList의 대문자와 같으면 제거
    # myList에서 
    for j in range(len(passList)):
        if ans[0] in passList[j][0].upper():
            pass
        elif ans == passList[j][0].upper():
            ans.remove()
"""


# myList의 첫글자를 대문자로 변환해 삽입
# 만약, myList의 첫 글자가 passList에 있는 문자라면 삽입 O.  
if myList[0] in passList:
    ans.append(myList[0][0].upper())
    
# 만약, myList의 글자 중 passList에 있는 문자가 있으면 삽입 X. 
# 인덱스 시발!!!!!
for i in myList :
    if not i in passList:
        ans.append(i[0].upper())

"""
# ans에서 passList 내용 中 첫글자 대문자와 일치하는것이 있으면 제거? 이러면 예외걸릴듯.
for i in range(len(ans)):
    for j in range(len(passList)) :
        if ans[i] in passList[j][0].upper() :
            ans.remove(ans[i])
"""
# i asm ali pa te nigger
# 출력형식 맞추기
for i in range(len(ans)) :
    print(ans[i], end='')
