from collections import deque
def Snake(arr, turn):
    count = 0
    # 방향 오른쪽부터 0, 1, 2, 3
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    queue = deque()
    path = deque()
    # (0, 0) 머리, (0, 0) 꼬리 방향 0
    queue.append((0, 0, 0))
    # 지나온 경로를 담을 큐
    path.append((0, 0))
    arr[0][0] = 2
    t = 0
    while queue:
        x, y, d = queue.popleft()
        # 가장 앞에 있는 회전 시간 비교하여 회전할 시간이면 회전
        if t < len(turn) and count == int(turn[t][0]):
            if turn[t][1] == 'L':
                d = (d - 1) % 4
            else:
                d = (d + 1) % 4
            t += 1
        # 시간 증가
        count += 1
        # 이동할 칸
        ax = x + dx[d]
        ay = y + dy[d]
        # 벽에 부딪히는지
        if 0 <= ax < N and 0 <= ay < N:
            # 사과면 꼬리가 줄지 않는다
            # 머리 큐와 경로 큐에 추가
            if arr[ax][ay] == 1:
                queue.append((ax, ay, d))
                arr[ax][ay] = 2
                path.append((ax, ay))
            # 사과가 없으면 경로 큐 pop하여 꼬리가 줄면서 0으로
            # 머리 큐와 경로 큐에 이동한 칸 추가
            elif arr[ax][ay] == 0:
                px, py = path.popleft()
                arr[px][py] = 0
                arr[ax][ay] = 2
                queue.append((ax, ay, d))
                path.append((ax, ay))
            # 이동한 칸이 2면 자기 몸에 부딪혀 stop
            else:
                break
        else:
            break

    return count

N = int(input())
arr = [[0] * N for _ in range(N)]
K = int(input())
for _ in range(K):
    a, b = map(int, input().split())
    arr[a-1][b-1] = 1
L = int(input())
turn = [input().split() for _ in range(L)]
print(Snake(arr, turn))