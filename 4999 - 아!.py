"""
aaah를 말해봐라.

의사는 aaaah 를 요청하기도, h를 요청하기도.

자기가 낼수있는 aaaah보다 같거나 짧은 의사한테만 방문.

가야 한다면 go, 아니라면 no 출력.
"""
speak = input()
doctor = input()

if len(speak) >= len(doctor) :
    print('go')
else:
    print('no')
