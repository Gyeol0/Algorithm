def bridge(N, M):
    dp = [0]*(N+1)
    dp[0] = 0
    dp[1] = M
    for i in range(2, N+1):
        dp[i] = dp[i-1] * (M- (i - 1)) // i
    return dp[N]
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    print(bridge(N, M))