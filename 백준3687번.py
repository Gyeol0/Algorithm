def Matchstick(N):
    """"
    2개 : 1
    3개 : 7
    4개 : 4
    5개 : 2, 3, 5
    6개 : 6, 9, 0
    7개 : 8
    짝수개면 무조건 1만 사용
    홀수개면 하나는 7로 사용
    """
    max_dp = [0] * (N+10)
    max_dp[2] = '1'
    max_dp[3] = '7'
    for i in range(4, N+1):
        max_dp[i] = max_dp[i-2] + '1'


    min_dp = [99999999999999999999999999] * (N+10)
    min_dp[2] = '1'
    min_dp[3] = '7'
    min_dp[4] = '4'
    min_dp[5] = '2'
    min_dp[6] = '6'
    min_dp[7] = '8'
    min_dp[8] = '10'
    for i in range(9, N+1):
        min_dp[i] = str(min(int(min_dp[i-2] + '1'), int(min_dp[i])))
        min_dp[i] = str(min(int(min_dp[i-3] + '7'), int(min_dp[i])))
        min_dp[i] = str(min(int(min_dp[i-4] + '4'), int(min_dp[i])))
        min_dp[i] = str(min(int(min_dp[i-5] + '2'), int(min_dp[i])))
        min_dp[i] = str(min(int(min_dp[i-6] + '0'), int(min_dp[i])))
        min_dp[i] = str(min(int(min_dp[i-7] + '8'), int(min_dp[i])))
    return min_dp[N], max_dp[N]

T= int(input())
for t in range(T):
    N = int(input())
    result = Matchstick(N)
    print(result[0], result[1])

