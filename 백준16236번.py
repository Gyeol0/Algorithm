from collections import deque

# bfs로 가장 가까운 먹이를 찾음
# 없으면 그만
def shark(N, start):
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]
    visit = [[0]*N for _ in range(N)]
    queue = deque()
    queue.append(start)
    e = []
    max_count = 999999
    while queue:
        x, y, count = queue.popleft()
        if count + 1 > max_count:
            break
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if 0 <= ax < N and 0 <= ay < N and not visit[ax][ay]:
                if 0 < arr[ax][ay] < size:
                    e.append((ax, ay, count + 1))
                    max_count = count + 1
                    visit[ax][ay] = 1
                elif arr[ax][ay] == size or arr[ax][ay] == 0:
                    queue.append((ax, ay, count + 1))
                    visit[ax][ay] = 1
    return e

size = 2
eat = 0
time = 0
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9:
            start = (i, j, 0)
            arr[i][j] = 0

while True:
    # 가장 가까운 먹이
    result = shark(N, start)
    if result:
        # 가장 위에 있고 왼쪽에 있는 먹이
        result = sorted(result, key = lambda x : (x[0], x[1]))[0]
        eat += 1
        if size == eat:
            size += 1
            eat = 0
        arr[result[0]][result[1]] = 0
        time += result[2]
        # 출발점 재조정
        start = (result[0], result[1], 0)
    else:
        break
print(time)
