import sys

# 입력받은 단어는 공백을 기준으로 나눈다.
myWord = list(input().split())

if len(myWord) > 1000000 :
    sys.exit(0)
    
print(len(myWord))