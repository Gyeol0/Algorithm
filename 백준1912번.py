def continuous(N, arr):
    dp = [0] * N
    dp[0] = arr[0]
    for i in range(1, N):
        dp[i] = max(dp[i-1] + arr[i], arr[i])
    return max(dp)
N = int(input())
arr = list(map(int, input().split()))
print(continuous(N, arr))