
"""
(x1,y1)부터 (x2,y2) 구간의 합은 (0,0)(x2,y2) - (0,0)(x1-1,y2) - (0,0)(x2,y1-1) + (0,0)(x1-1)(y1-1)
A B
C D
구하려는 구간 = D
A + B + C + D = arr에 저장되어 있는 합, (0,0)부터 (x2,y2)까지의 합
D = (A + B + C +D) - (A + C) - (A + B) + A
"""
import sys
N, M = map(int, input().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
# (0, 0)부터 (i, j)까지의 사각형 합을 구한 값을 저장해놓는다.

# 가로줄 더하기
for i in range(N):
    for j in range(1, N):
        arr[i][j] += arr[i][j-1]
# 세로줄 더하기
for i in range(1, N):
    for j in range(N):
        arr[i][j] += arr[i-1][j]

for i in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == 1 and y1 == 1: # 내가 만든 행렬에서는 0, 0
        print(arr[x2-1][y2-1])
    # 맨 윗줄에 붙어 있음, 왼쪽 사각형만 떼어주면됨, (0,0)(x2,y2) - (0,0)(x2,y1-1)
    elif x1 == 1:
        print(arr[x2-1][y2-1] - arr[x2-1][y1-2])
    # 맨 왼쪽줄에 붙어 있음, 오른쪽 위 사각형만 떼어주면됨, (0,0)(x2,y2) - (0,0)(x1-1,y2)
    elif y1 == 1:
        print(arr[x2-1][y2-1] - arr[x1-2][y2-1])
    else:
        print(arr[x2-1][y2-1] - arr[x2-1][y1-2] - arr[x1-2][y2-1] + arr[x1-2][y1-2])