def drink(N, P):
    dp = [0] * N
    dp[0] = P[0]
    if N > 1:
        dp[1] = P[0] + P[1]
    """
    이러한 문제를 풀 때, 조건을 먼저 생각해서 현재 상황에서 조건을 만족하는 경우를 모두 만들고, 이들끼리 비교한다.
    
    현재의 포도주를 먹으려면 이전의 포두주와 같이 확인
    1. 현재 포도구 먹고 이전 포도주 안먹음
     - 이전 포도주 안먹었으니까 dp[i-2] 
    2. 현재와 이전 포도주 둘 다 먹음
     - 둘 다 먹으려면 전전은 먹으면 안됨, dp[i-3]
    3. 현재 포도주 안먹음
     - dp[i-1]
    3가지 경우를 모두 확인해서 최댓값을 넣어줌
    """
    for i in range(2, N):
        c1 = P[i] + dp[i - 2]
        c2 = P[i] + P[i - 1] + dp[i - 3]
        c3 = dp[i - 1]
        dp[i] = max(c1, c2, c3)

    return dp[-1]

N = int(input())
P = [int(input()) for _ in range(N)]
print(drink(N, P))