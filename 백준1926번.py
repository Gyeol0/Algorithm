from collections import deque
def bfs(arr):
    max_area = 0
    cnt = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    for i in range(N):
        for j in range(M):
            # 구역 탐색
            if arr[i][j] == 1:
                # 영역 개수 +1
                cnt += 1
                queue = deque()
                queue.append((i, j))
                arr[i][j] = 0
                # 넓이 계산
                area = 1
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        ax = x + dx[k]
                        ay = y + dy[k]
                        if 0 <= ax < N and 0 <= ay < M:
                            if arr[ax][ay] == 1:
                                queue.append((ax, ay))
                                area += 1
                                arr[ax][ay] = 0
                # 최댓값 비교
                max_area = max(max_area, area)
    return cnt, max_area

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt, max_area = bfs(arr)
print(cnt)
print(max_area)