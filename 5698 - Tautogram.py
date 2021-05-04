import sys

# Tautogram인지 확인하는 함수 정의.
def checkTauto(sentence) :
    for i in sentence :
        if(i[0][0] != sentence[0][0]) :
            checker = 'N'
            break
        else :
            checker = 'Y'
    return checker 

resultBox = [] # 결과(Y/N)를 담을 리스트.

while True :
    # 대소문자 구분없이 동일한지 확인하면 됨. 입력받을때부터 소문자로 치환.    
    mySen = list(input().lower().split())
    
    # 입력이 *이면 break.
    if mySen[0] == '*' :
        break
    
    # 예외처리.
    # 글자수가 50을 넘기는 경우
    if len(mySen) > 50 :
        sys.exit(0)
    # 입력된 단어의 길이가 20자를 넘는경우
    for i in range(len(mySen)) :
        if len(mySen[i]) > 20: # 확인 잘 하자... 이거때문에 자꾸 틀렸다...
            sys.exit(0)
    
    # 결과 박스에 함수 실행 결과를 담음.
    resultBox.append(checkTauto(mySen))

# 출력 형식에 맞춰 출력.
for i in range(len(resultBox)):
    print(resultBox[i], sep = '\n')
