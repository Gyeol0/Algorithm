def drink(N, P):
    dp = [0] * N
    dp[0] = P[0]
    if N > 1:
        dp[1] = P[0] + P[1]
    """
    1. 이전 포도주 안먹고 현재 포도주 먹기
    2. 이전과 현재 포도주 모두 먹음
    3. 현재 포도주 안먹음
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