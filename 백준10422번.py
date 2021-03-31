def par():
    dp = [0] * 5001
    dp[0] = 1
    # 홀 수는 무조건 0
    for i in range(2, 5001, 2):
        for j in range(2, i + 1, 2):
            dp[i] += (dp[j - 2] * dp[i-j]) % 1000000007

    return dp

T = int(input())
num = [int(input()) for _ in range(T)]
dp = par()
for n in num:
    print(dp[n] % 1000000007)