def checkPita(x, y, z) :
    if z**2 == x**2 + y**2 :
        return print('right')
    else :
        return print('wrong')

#a, b, c = map(int, input().split())

#checkPita(a,b,c)

while True :
    # a, b, c = map(int, input().split())
    myList = list(map(int, input().split()))
    pitaList = sorted(myList)
    if pitaList[0] == 0 and pitaList[1] == 0 and pitaList[2] == 0:
        break
    
    checkPita(pitaList[0], pitaList[1], pitaList[2])
    