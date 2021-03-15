def stone_game(N):
    dp = [0]*(N+2)
    dp[1] = 'SK'
    dp[2] = 'CY'
    for i in range(3, N+1):
        if dp[i-1] == 'SK':
            dp[i] = 'CY'
        else:
            dp[i] = 'SK'
    return dp[N]


N = int(input())
print(stone_game(N))
# if N % 2 == 0:
#     print('CY')
# else:
#     print('SK')