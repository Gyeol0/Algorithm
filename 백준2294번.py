def coin(n, k, c):
    dp = [999999999] * (k + 1)
    dp[0] = 0
    """
    경우의 수를 찾을 때에는 동전부터 돌렸지만
    최소 동전 개수이므로 dp부터 해도 된다.
    반대로 해도 둘 다 맞다.
    경우의 수일 때는 중복을 피하는 것이 중요
    """
    for i in range(1, k + 1):
        for j in c:
            if i - j >= 0:
                dp[i] = min(dp[i], dp[i-j] + 1)
    if dp[-1] == 999999999:
        return -1
    return dp[-1]

n, k = map(int, input().split())
c = [int(input()) for _ in range(n)]
print(coin(n, k, c))