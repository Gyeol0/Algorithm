def four_squares(N):
    # 다이나믹 프로그래밍
    dp = [0] * (N + 1)
    dp[1] = 1
    for i in range(2, N+1):
        j = 1
        min_dp = 99999999999999

        # 포함하는 제곱값 중에서 n에서 제곱값을 뺀 dp의 최솟값 찾기
        # 찾은 dp에 1을 더해주면(찾은 제곱값) dp[i]가 나온다.

        while j ** 2 <= i:
            min_dp = min(dp[i - (j**2)], min_dp)
            j += 1
        dp[i] = min_dp + 1
    return dp[-1]

def four_squares2(N):
    # 브루트 포스
    # 브루트 포스가 더 빠르다.
    # 무조건 4개 이하
    # 1개일 때
    if int(N ** 0.5) ** 2 == N:
        return 1
    # 2개일 때
    for i in range(1, int(N**0.5) + 1):
        if int((N - i ** 2) ** 0.5) ** 2 == (N - i ** 2):
            return 2
    # 3개 일 때
    for i in range(1, int(N**0.5) + 1):
        for j in range(1, int((N - i ** 2)**0.5) + 1):
            if int((N - i ** 2 - j **2) ** 0.5) ** 2 == (N - i ** 2 - j**2):
                return 3
    return 4
N = int(input())
print(four_squares2(N))