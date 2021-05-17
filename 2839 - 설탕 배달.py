# N = 배달해야하는 설탕 무게.
N = int(input())

# 봉지는 3kg, 5kg가 있음.
# 최대한 적은 봉지 수로 배달.
# ex) N=18이면, 3kg * 1개 + 5kg * 3개 로 배달. (3kg * 6개는 X)

# 3과 5를 최소 횟수로 더한다. --> Greedy?
# 주어진 N에 대해, 3과 5의 최소공배수? 뭐라해야되지... 
    # 우선 5로 나눠 떨어지는지 확인하고, 나눠 떨어지면 몫 == 봉지 수
     ## N이 3으로 나눠 떨어진다면, ㄴㄴㄴㄴㄴ 이건 아닌듯. 
    # 아니라면 N-3이 5로 나눠지는지 확인. 그래도 아니면? 3kg짜리를 하나 들어야한다.
    # 계속 이짓 하다가 --> while True // N이 음수가 되면? break하고 -1 출력하면 될것. 
    
toCarry = 0
while True :
    # 5로 나눠 떨어지게 되면 N/5의 몫이 toCarry.
    if N % 5 == 0 :
        toCarry += N // 5
        print(toCarry)
        break
    # 5로 나눠 안떨어지면 3kg짜리 하나는 들어야함. (N에서 3빼주고 toCarry는 1 늘어나는 셈.)
    N -= 3
    toCarry += 1
    # N이 음수되면 가진 봉지로는 못들고감.
    if N < 0 :
        print('-1')
        break