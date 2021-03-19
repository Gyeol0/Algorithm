def coin(n, k, c):
    dp = [0] * (k + 1)
    dp[0] = 1
    for i in range(n):
        for j in range(1, k + 1):
            if j - c[i] >= 0:
                dp[j] += dp[j-c[i]]

    return dp[-1]

n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
print(coin(n, k, c))