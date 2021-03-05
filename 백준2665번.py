from collections import deque
# 힙으로도 풀 수가 있다.
#     dist = [[N*N] * N for _ in range(N) 거리 계산하여 넣을 행렬
#     while queue:
#         count, x, y = heapq.heappop(queue)
#
#         for k in range(4):
#             ax = x + dx[k]
#             ay = y + dy[k]
#             if 0 <= ax < N and 0 <= ay < N:
#                 if count + 1 < dist[ax][ay]: 검은 방일 때 신경써야하므로 +1 한게 더 작으면 방문하고 변경
#                     if arr[ax][ay] == 0:
#                         heapq.heappush(queue, [count + 1, ax, ay])
#                         dist[ax][ay] = count + 1
#                     else:
#                         heapq.heappush(queue, [count, ax, ay])
#                         dist[ax][ay] = count
#     return dist[n-1][n-1]
def bfs(N, arr):
    min_count = N*N
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    queue = deque()
    # 시작점이 검은방인지 흰방인지
    if arr[0][0] == '1':
        queue.append((0, 0, 0))
        arr[0][0] = '10'
    else:
        arr[0][0] = '01'
        queue.append((0, 0, 1))

    while queue:
        # 네 방향 탐색
        x, y, count = queue.popleft()
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            if 0 <= ax < N and 0 <= ay < N:
                # 도착하면 최솟값 비교
                if ax == N-1 and ay == N-1:
                    min_count = min(min_count, count)
                    continue
                # 처음 간 흰방이면, 여기까지의 최솟값으로 변환
                if arr[ax][ay] == '1':
                    queue.append((ax, ay, count))
                    arr[ax][ay] = '1' + str(count)
                # 처음 간 검은방이면, 여기까지의 최솟값으로 변환
                elif arr[ax][ay] == '0':
                    queue.append((ax, ay, count + 1))
                    arr[ax][ay] = '0' + str(count + 1)
                else:
                    # 이미 갔던 방이면, 현재까지의 최솟값과 비교하여 더 작으면 바꾸고 큐에 삽입
                    if arr[ax][ay][0] == '0':
                        if int(arr[ax][ay][1:]) > count + 1:
                            arr[ax][ay] = '0' + str(count + 1)
                            queue.append((ax, ay, count + 1))
                    else:
                        if int(arr[ax][ay][1:]) > count:
                            arr[ax][ay] = '1' + str(count)
                            queue.append((ax, ay, count))
    return min_count
N = int(input())
arr = [list(input()) for _ in range(N)]
print(bfs(N, arr))