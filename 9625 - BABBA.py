"""
처음엔 A부터 시작.

A는 B로 바뀐다
B는 BA로 바뀐다.

이를 K번 눌렀을때 A,B는 총 몇개일까
"""
K = int(input())
"""
# 처음은 A.
# 누를때마다 A는 B, B는 BA로.

word = 'A'

# print(word.replace('A', 'B')) # A to B
# print(word.replace('B', 'BA')) # B to BA
counter = 0
"""
"""
for i in range(K):
    # A to B
    word = word.replace('A', 'B') 
    counter += 1
    
    if counter == K:
        break
    
    # B to BA
    word = word.replace('B', 'BA')
    
0 A - 1 0
1 B - 0 1
2 BA - 1 1
3 BAB - 1 2
4 BABBA - 2 3
5 BABBABAB - 3 5
6 BABBABABBABBA - 5 8
7 BABBABABBABBABABBABAB - 8 13

이거 피보나치 수열 아닌가
"""
"""
while True:
    if counter == K:
        break
    
    # 한번 누르면 A -> B
    counter += 1
    word = word.replace('A', 'B')
    if counter == K:
        break
    
    # 또 한번 누르면 B -> BA
    counter += 1
    word = word.replace('B', 'BA')
    if counter == K:
        break
"""    
# print(word)
# print(word.count('A'), word.count('B'))

# A, B 갯수 보니까 피보나치 수열 같다.
# 버튼누르는거로 해결하는게 아닌듯
# wordA, wordB = [0]*K, [0]*K

# K가 45이하니까 45짜리 만들어두는게 나을듯.
wordA = [0]*46
wordB = [0]*46

# 초기값 설정
wordA[0], wordA[1] = 1, 0
wordB[0], wordB[1] = 0, 1
for i in range(2, 46):
    """
    if K == 1:
        wordA[0] = 1
        wordB[0] = 0
        print(wordA[0], wordB[0])
        break
    if K == 2:
        wordA[0], wordA[1] = 1, 0
        wordB[0], wordB[1] = 0, 1
        print(wordA[1], wordB[1])
        break
    """
    wordA[i] = wordA[i-1] + wordA[i-2]
    wordB[i] = wordB[i-1] + wordB[i-2]

print(wordA[K], wordB[K])