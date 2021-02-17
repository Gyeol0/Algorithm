def Move_Pipe(i, j, direction):
    global answer
    global P
    global N
    # 도착, 종료
    if i == N-1 and j == N-1:
        answer += 1
        return
    # 가로 방향
    if direction == 1:
        # 가로 방향 이동
        if j+1 < N and P[i][j+1] == 0:
            Move_Pipe(i, j+1, 1)
            # 대각선 방향 이동
            if i+1 < N and P[i+1][j] == 0 and P[i+1][j+1] == 0:
                Move_Pipe(i+1, j+1, 3)
    # 세로 방향
    elif direction == 2:
        # 세로 방향 이동
        if i+1 < N and P[i+1][j] == 0:
            Move_Pipe(i+1, j, 2)
            # 대각선 방향 이동
            if j+1 < N and P[i][j+1] == 0 and P[i+1][j+1] == 0:
                Move_Pipe(i+1, j+1, 3)
    # 대각선 방향
    elif direction == 3:
        # 가로 방향 이동
        if j+1 < N and P[i][j+1] == 0:
            Move_Pipe(i, j+1, 1)
        # 세로 방향 이동
        if i+1 < N and P[i+1][j] == 0:
            Move_Pipe(i+1, j, 2)
        # 대각선 이동
        if i+1 < N and j+1 < N and P[i][j+1] == 0 and P[i+1][j] == 0 and P[i+1][j+1] == 0:
            Move_Pipe(i+1, j+1, 3)

N = int(input())
P = []
answer = 0
for _ in range(N):
    P.append(list(map(int, input().split())))
Move_Pipe(0, 1, 1)
print(answer)