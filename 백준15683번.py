# 0일때는 7로 바꾸고 7부터는 1씩 증가, 겹칠 수 있으므로, 겹친 것을 지우면 오류
def change(arr, x, y, dx, dy, p, i):
    # 감시
    if p == 1:
        # 보이는 방향 모두 바꾸기
        for k in range(len(dx[i])):
            px = x
            py = y
            while True:
                ax = px + dx[i][k]
                ay = py + dy[i][k]
                if 0 <= ax < N and 0 <= ay < M:
                    # 0이면 7로
                    if arr[ax][ay] == 0:
                        arr[ax][ay] = 7
                    # 7부터는 1씩 증가
                    elif arr[ax][ay] > 6:
                        arr[ax][ay] += 1
                    # 벽이면 그만
                    elif arr[ax][ay] == 6:
                        break
                # 범위 넘어가면 그만
                else:
                    break
                px = ax
                py = ay
    else:
        # 되돌리기
        for k in range(len(dx[i])):
            px = x
            py = y
            while True:
                ax = px + dx[i][k]
                ay = py + dy[i][k]
                if 0 <= ax < N and 0 <= ay < M:
                    if arr[ax][ay] > 7:
                        arr[ax][ay] -= 1
                    elif arr[ax][ay] == 7:
                        arr[ax][ay] = 0
                    elif arr[ax][ay] == 6:
                        break
                else:
                    break
                px = ax
                py = ay
    return arr

# 사각지대 개수 체크
def check(arr, N, M):
    count = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                count += 1
    return count

# 완전 탐색 재귀문(DFS)
def CCTV(arr, x, y):
    global min_count
    # x축 다 돌면(맨밑) y축 하나 증가 시키고 맨 위로
    if x == N:
        CCTV(arr, 0, y + 1)
        return
    # y축도 다 돌면 사각지대 검사
    if y == M:
        count = check(arr, N, M)
        min_count = min(min_count, count)
        return

    # 현재 위치에 cctv가 있으면 cctv 별로 감시
    if arr[x][y] == 1:
        for i in range(4):
            # 바꾸고
            arr = change(arr, x, y, dx1, dy1, 1, i)
            CCTV(arr, x + 1, y)
            # 되돌리기
            arr = change(arr, x, y, dx1, dy1, 0, i)
    elif arr[x][y] == 2:
        for i in range(2):
            arr = change(arr, x, y, dx2, dy2, 1, i)
            CCTV(arr, x + 1, y)
            arr = change(arr, x, y, dx2, dy2, 0, i)
    elif arr[x][y] == 3:
        for i in range(4):
            arr = change(arr, x, y, dx3, dy3, 1, i)
            CCTV(arr, x + 1, y)
            arr = change(arr, x, y, dx3, dy3, 0, i)
    elif arr[x][y] == 4:
        for i in range(4):
            arr = change(arr, x, y, dx4, dy4, 1, i)
            CCTV(arr, x + 1, y)
            arr = change(arr, x, y, dx4, dy4, 0, i)
    elif arr[x][y] == 5:
        for i in range(1):
            arr = change(arr, x, y, dx5, dy5, 1, i)
            CCTV(arr, x + 1, y)
            arr = change(arr, x, y, dx5, dy5, 0, i)
    else:
        # 없으면 그냥 지나감
        CCTV(arr, x + 1, y)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# N, M이 최대 8이므로 최대 64
min_count = 64
# CCTV별로 회전했을 때 가능한 방향
dx1 = [[0], [1], [0], [-1]]
dy1 = [[1], [0], [-1], [0]]
dx2 = [[0, 0], [1, -1]]
dy2 = [[1, -1], [0, 0]]
dx3 = [[-1, 0], [0, 1], [1, 0], [0, -1]]
dy3 = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dx4 = [[0, -1, 0], [-1, 0, 1], [0, 1, 0], [1, 0, -1]]
dy4 = [[-1, 0, 1], [0, 1, 0], [1, 0, -1], [0, -1, 0]]
dx5 = [[1, -1, 0, 0]]
dy5 = [[0, 0, -1, 1]]
CCTV(arr, 0, 0)
print(min_count)
