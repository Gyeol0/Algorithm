# 흰색 칸으로 이동할 떄
# 위에 쌓여 있는 것 가져가고 위치 piece에서 바꿔주기, 방향은 그대로
def white(x, y, ax, ay, d, n):
    k = visit[x][y].index(n)
    for p in visit[x][y][k:]:
        piece[p][0] = ax
        piece[p][1] = ay
        visit[ax][ay].append(p)
    visit[x][y] = visit[x][y][:k]

# 빨간 칸으로 이동할 때
# 위에 쌓여 있는 것 뒤집어서 가져가서 위치 piece에서 바꿔주기, 방향은 그대로
def red(x, y, ax, ay, d, n):
    k = visit[x][y].index(n)
    move = []
    for p in visit[x][y][k:]:
        piece[p][0] = ax
        piece[p][1] = ay
        move.insert(0, p)
    visit[ax][ay].extend(move)
    visit[x][y] = visit[x][y][:k]

# 파란 칸으로 이동할 떄
# 방향 반대로 바꿔서 이동할 수 있으면 이동
# 바꾼 방향 piece에서도 바꿔주고 이동
def blue(x, y, d, n):
    if d == 1:
        d = 2
    elif d == 2:
        d = 1
    elif d == 3:
        d = 4
    elif d == 4:
        d = 3
    ax = x + dx[d]
    ay = y + dy[d]
    piece[n][2] = d
    if 0 < ax <= N and 0 < ay <= N:
        # 흰색 칸일 떄
        if arr[ax-1][ay-1] == 0:
            white(x, y, ax, ay, d, n)
            return len(visit[ax][ay])
        # 빨간 칸일 때
        elif arr[ax-1][ay-1] == 1:
            red(x, y, ax, ay, d, n)
            return len(visit[ax][ay])
    return 0
def game(arr, piece, visit):
    for c in range(1, 1001):
        for i in range(K):
            x, y, d = piece[i]
            ax = x + dx[d]
            ay = y + dy[d]
            if 0 < ax <= N and 0 < ay <= N:
                # 흰색 칸일 떄
                if arr[ax-1][ay-1] == 0:
                    white(x, y, ax, ay, d, i)
                    # 이동했을 때 4개 이상이 되면 그만
                    if len(visit[ax][ay]) >= 4:
                        return c
                # 빨간 칸일 때
                elif arr[ax-1][ay-1] == 1:
                    red(x, y, ax, ay, d, i)
                    # 이동했을 때 4개 이상이 되면 그만
                    if len(visit[ax][ay]) >= 4:
                        return c
                # 파란 칸일 때
                else:
                    count = blue(x, y, d, i)
                    # 이동했을 때 4개 이상이 되면 그만
                    if count >= 4:
                        return c
            else:
                count = blue(x, y, d, i)
                # 이동했을 때 4개 이상이 되면 그만
                if count >= 4:
                    return c
    # 1000번 동안 4개 이상 안 모일 때
    return -1

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
piece = [list(map(int, input().split())) for _ in range(K)]
visit = [[[] for i in range(N+1)] for _ in range(N+1)]
dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]
for i in range(K):
    x, y, d = piece[i]
    visit[x][y].append(i)
print(game(arr, piece, visit))