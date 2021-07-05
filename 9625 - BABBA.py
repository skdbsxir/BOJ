"""
처음엔 A부터 시작.

A는 B로 바뀐다
B는 BA로 바뀐다.

이를 K번 눌렀을때 A,B는 총 몇개일까
"""
K = int(input())

# 처음은 A.
# 누를때마다 A는 B, B는 BA로.

word = 'A'

# print(word.replace('A', 'B')) # A to B
# print(word.replace('B', 'BA')) # B to BA
counter = 0

"""
for i in range(K):
    # A to B
    word = word.replace('A', 'B') 
    counter += 1
    
    if counter == K:
        break
    
    # B to BA
    word = word.replace('B', 'BA')
    
A B BA BAB BABBA
"""
while True:
    if counter == K:
        break
    
    word = word.replace('A', 'B')
    counter += 1
    if counter == K:
        break
    
    word = word.replace('B', 'BA')
    counter += 1
    if counter == K:
        break
    
print(word)