def plus(N):
    if N <= 3:
        if N == 1:
            return 1
        elif N == 2:
            return 2
        else:
            return 4
    dp = [0]*(N+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4
    # dp[i]에 i를 만드는 경우의 수 저장
    for i in range(4, N+1):
        dp[i] = dp[i-3] + dp[i-2] + dp[i-1]

    return dp[-1]
T = int(input())
for t in range(T):
    N = int(input())
    print(plus(N))