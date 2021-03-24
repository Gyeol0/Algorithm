def stairs(N):
    # 2차원에는 오른쪽 수가 k인 개수를 넣어 둘 것
    # dp[i][1] = 맨 오른쪽 수가 1인 개수
    dp = [[0]*10 for _ in range(N + 1)]
    for i in range(1, 10):
        dp[1][i] = 1
    # 맨 오른쪽 수에 +1 또는 -1 값을 붙여주기만 하면 되는데
    # 9 옆에는 8만 붙이고, 0 옆에는 1만 붙일 수 있기 때문에 조건문 달고 나머지는 +1, -1
    for i in range(2, N + 1):
        for j in range(10):
            if j == 0:
                dp[i][j] += dp[i-1][1]
            elif j == 9:
                dp[i][j] += dp[i-1][8]
            else:
                dp[i][j] += dp[i-1][j-1]
                dp[i][j] += dp[i-1][j+1]

    return sum(dp[-1]) % 1000000000

N = int(input())
print(stairs(N))