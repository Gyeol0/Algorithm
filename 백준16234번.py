from collections import deque
# 인구 이동 한 번
def People(N, arr):
    global c
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    flag = False
    # 방문하지 않은 곳에서 bfs
    for i in range(N):
        for j in range(N):
            if visit[i][j] == c:
                queue.append((i, j))
                # 인구 이동할 구간
                path = [(i, j)]
                count = 1
                # 인구 합
                sum_people = arr[i][j]
                visit[i][j] = c+1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        ax = x + dx[k]
                        ay = y + dy[k]
                        if 0 <= ax < N and 0 <= ay < N and visit[ax][ay] == c:
                            # 경계선을 열지 확인
                            if L <= abs(arr[ax][ay] - arr[x][y]) <= R:
                                visit[ax][ay] = c+1
                                count += 1
                                queue.append((ax, ay))
                                sum_people += arr[ax][ay]
                                path.append((ax, ay))
                # 인구 이동하면 True, 변화 없으면 False
                # 인구 이동
                for p in path:
                    if arr[p[0]][p[1]] != sum_people // count:
                        flag = True
                    arr[p[0]][p[1]] = sum_people // count
    return flag

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
visit = [[0]*N for _ in range(N)]
c = 0
# 인구이동이 진행되면 계속
while People(N, arr):
    c += 1
    result += 1
print(result)