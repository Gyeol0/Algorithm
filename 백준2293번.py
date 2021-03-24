def coin(n, k, c):
    dp = [0] * (k + 1)
    dp[0] = 1
    # 경우의 수는 동전이 먼저
    # dp부터 for문을 하면 동전끼리 중복이 있어서 수가 급격하게 증가함
    # 중복을 없애면서 동전마다 for문을 돌림
    for i in range(n):
        for j in range(1, k + 1):
            if j - c[i] >= 0:
                dp[j] += dp[j-c[i]]

    return dp[-1]

n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
print(coin(n, k, c))