"""
탁자 위 돌 N개. A와 B. 턴을 번갈아 가면서 돌을 가져감. 

돌은 1개 or 3개만 가져갈 수 있음.
마지막 돌을 가져가는 사람이 승리.

두 사람이 완벽히 게임을 했을때, 이기는 사람을 구하는 프로그램 작성.

게임은 A가 먼저 시작.

입력 : N
출력 : 이기는사람. A - SK, B - CY
"""
N = int(input())

"""
def simulation(N):
    # N = 1이면 A가 무조건 승리
    if N == 1:
        winner = 'SK'
    # N = 2이면 B가 무조건 승리
    elif N == 2:
        winner = 'CY'
    # N = 3이면 A가 무조건 승리
    elif N == 3:
        winner = 'SK'
        
    return winner
"""
"""
게임은 한쪽이 이기려고 하는 거. 양보나 그딴거 X.

4 - 1,3 / 3,1 -> B가 무조건 승리
5 - 1,1,3 / 1,3,1 / 3,1,1 -> A가 무조건 승리
6 - 1,3,1,1 / 1,1,3,1 / 1,1,1,1,1,1 / 3,3 / 3,1,1,1 -> B가 무조건 승리

홀수일땐 A가 이기고, 짝수일땐 B가 이기고 아닌가?
"""
def simulation(N):
    # 홀수면 A가 무조건 승리
    if N % 2 == 1:
        winner = 'SK'
    # 짝수면 B가 무조건 승리
    elif N % 2 == 0:
        winner = 'CY'
    
    return winner

print(simulation(N))