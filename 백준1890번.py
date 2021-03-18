# 처음에는 재귀로 풀려했는데 무조건 시간이 초과된다.
# 그냥 반복문이 훨씬 빠르다.
def jump(N, arr):
    dp = [[0] * N for _ in range(N)]
    dp[0][0] = 1
    for x in range(N):
        for y in range(N):
            if x == N - 1 and y == N - 1:
                return dp[N-1][N-1]
            k = arr[x][y]
            ax = x + k
            ay = y + k
            if ax < N:
                dp[ax][y] += dp[x][y]
            if ay < N:
                dp[x][ay] += dp[x][y]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(jump(N, arr))

