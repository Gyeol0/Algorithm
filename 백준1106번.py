def hotel(C, H, N):
    dp = [99999999] * (C + 1)
    # dp[i]에는 i명을 데리고 올 때 최소 비용
    dp[0] = 0
    for i in range(1, C + 1):
        for j in range(N):
            # 몇 명을 잡아올지를 결정하기 위해서 모두 비교
            # 현재 필요한거보다 너무 많이 데려오면 넘치지만 효율이 좋을 수도 있다.
            # 그래서 넘칠 때에는 그 사람 데리올 때의 비용과 비교
            if i - H[j][1] < 0:
                dp[i] = min(dp[i], H[j][0])
            else:
                # 안넘치면 거기에 이 사람들 데리고 오는 비용 더해서 비교
                dp[i] = min(dp[i - H[j][1]] + H[j][0], dp[i])

    return dp[-1]

C, N = map(int, input().split())
H = [list(map(int, input().split())) for _ in range(N)]
print(hotel(C, H, N))