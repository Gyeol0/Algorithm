def Paper(N):
    dp = []
    dp.append(1)
    dp.append(3)
    for i in range(2,N):
        dp.append(dp[i-1] + dp[i-2] * 2)
    return dp[N-1]
N = int(input())
print(Paper(N) % 10007)