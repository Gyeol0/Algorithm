import sys
"""
냅색 문제
dp 리스트를 만들어 놓고, 각 물건마다 넣으면 좋을 지 판단
내부 for문을 반대로 도는 이유는, 정방향으로 할 때, 효율 좋은 물건은 중복으로 가져가려 하기 때문에 반대로
이 무게 전의 dp에 이 물건의 가치를 더 했을 때, 더 좋은 것인가를 판단 
"""
def bag(K, product):
    dp = [0] * (K + 1)
    for i in product:
        for j in range(K, i[0] -1, -1):
            dp[j] = max(dp[j], dp[j-i[0]] + i[1])
    return dp[K]

N, K =map(int, input().split())
product = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
print(bag(K, product))