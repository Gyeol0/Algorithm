def prefix(r1, c1, r2, c2, arr):
    # 전체 합
    all_sum = arr[max(r1, r2) - 1][max(c1, c2) - 1]
    # 맨 왼쪽에 붙어 있을 때
    if min(c1, c2) - 2 < 0:
        square1 = 0
    else:
        square1 = arr[max(r1, r2) - 1][min(c1, c2) - 2]
    # 맨 위에 붙어 있을 때
    if min(r1, r2) - 2 < 0:
        square2 = 0
    else:
        square2 = arr[min(r1, r2) - 2][max(c1, c2) - 1]
    if min(c1, c2) - 2 < 0 or min(r1, r2) - 2 < 0:
        square3 = 0
    else:
        square3 = arr[min(r1, r2) - 2][min(c1, c2) - 2]

    count = (abs(r1 - r2) + 1) * (abs(c1 - c2) + 1)
    answer = all_sum - square1 - square2 + square3
    answer = answer // count

    return answer


R, C, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
# 가로 합
for i in range(R):
    for j in range(1, C):
        arr[i][j] += arr[i][j-1]
# 세로 합
for i in range(C):
    for j in range(1, R):
        arr[j][i] += arr[j-1][i]

for t in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    print(prefix(r1, c1, r2, c2, arr))