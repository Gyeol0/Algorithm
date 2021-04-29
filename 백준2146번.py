from collections import deque
def bfs(arr):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    area = 2
    # 지역 나누기
    # area 1씩 증가시켜서 숫자로 구분
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                arr[i][j] = area
                queue = deque()
                queue.append((i, j))
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        ax = x + dx[k]
                        ay = y + dy[k]
                        if 0 <= ax < N and 0 <= ay < N:
                            if arr[ax][ay] == 1:
                                queue.append((ax, ay))
                                arr[ax][ay] = area
                area += 1
    # 다리 만드는 것을 flag로 표시
    # area와 헷갈리지 않도록 최대 area보다 큰 숫자부터 시작
    min_value = 999999999999
    flag = area + 1
    for i in range(N):
        for j in range(N):
            # 0이 아니면서 최대 area보다 작은 수
            # 즉, 나눠진 섬일 때
            if 0 < arr[i][j] < area:
                stop = False
                queue = deque()
                queue.append((i, j, 0))
                current = arr[i][j]
                # 탐색
                while queue:
                    x, y, cnt = queue.popleft()
                    if stop:
                        break
                    for k in range(4):
                        ax = x + dx[k]
                        ay = y + dy[k]
                        if 0 <= ax < N and 0 <= ay < N:
                            # 0이거나 섬이 아닌 flag
                            # flag는 예전에 놨던 다리들, 지금은 상관없음, 빈칸과도 같음
                            if arr[ax][ay] == 0 or area < arr[ax][ay] < flag:
                                queue.append((ax, ay, cnt + 1))
                                # 방문 표시
                                arr[ax][ay] = flag
                            # 현재 출발한 섬이 아니고, 최대 area보다 작은 => 다른 섬일 때
                            elif arr[ax][ay] != current and arr[ax][ay] <= area:
                                # 비교
                                min_value = min(min_value, cnt)
                                stop = True
                                break
                flag += 1
    return min_value

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs(arr))