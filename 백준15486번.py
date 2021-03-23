import sys
def resign(N, T):
    dp = [0] * (N + 1)
    for i in range(N):
        # 상담이 가능한지 확인
        if i + T[i][0] <= N:
            # 상담을 하는 것이 이득이지 그냥 있는게 이득인지 비교
            dp[i + T[i][0]] = max(dp[i] + T[i][1], dp[i + T[i][0]])
        # 현재까지의 최댓값으로 계속 바꿔준다.
        dp[i + 1] = max(dp[i], dp[i + 1])
    return max(dp)

N = int(input())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(resign(N, T))