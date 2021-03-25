def coin(N, coins, M):
    """
    dp[i] i원을 만드는 경우의 수
    경우의 수 이므로 가장 바깥 for문은 코인으로 돌린다.
    금액으로 돌리면 중복이 일어난다.
    """""
    dp = [0] * (M + 1)
    dp[0] = 1

    for i in coins:
        for k in range(1, M + 1):
            if k-i >= 0:
                dp[k] += dp[k-i]

    return dp[M]

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    print(coin(N, coins, M))
