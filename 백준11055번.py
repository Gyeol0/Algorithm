def sum_sequence(N, arr):
    dp = [0] * N
    # 현재 수
    for i in range(N):
        max_value = 0
        # 현재 수까지의 경우
        for j in range(i):
            # 만약 현재 수가 더 크면 그 때까지의 dp, 즉 그 때까지의 최대 값 계속 저장하면서
            # max_value 최신화
            if arr[i] > arr[j]:
                max_value = max(max_value, dp[j])

        # 현재 수에 오기까지의 최대 값 + 자기 자신
        dp[i] = max_value + arr[i]
    return max(dp)

N = int(input())
arr = list(map(int, input().split()))
print(sum_sequence(N, arr))