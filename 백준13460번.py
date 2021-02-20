from _collections import deque
def Bead(N, M, arr):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1
    # 막힐 때까지 중력으로 구슬을 옮기는 메소드
    def Move(ax, ay, k):
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]
        step = 0
        while True:
            step += 1
            ax = ax + dx[k]
            ay = ay + dy[k]
            if 0 <= ax < N and 0 <= ay < M:
                # 구멍으로 들어감
                if arr[ax][ay] == 'O':
                    return [ax,ay, step]
                # 벽에 막힘
                elif arr[ax][ay] == '#':
                    return [ax-dx[k],ay-dy[k],step-1]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 'R':
                red = [i,j]
            elif arr[i][j] == 'B':
                blue = [i,j]
            elif arr[i][j] == 'O':
                hole = [i,j]
    rx = red[0]
    ry = red[1]
    bx = blue[0]
    by = blue[1]
    queue = deque()
    queue.append([rx, ry, bx, by, 0])
    while queue:
        rx, ry, bx, by, count = queue.popleft()
        # 10번 이하로 못들어가서 return -1
        if count == 10:
            return -1
        for k in range(4):
            # RED와 BLUE 모두 중력으로 옮기기
            bbx, bby, step_b = Move(bx, by, k)
            arx, ary, step_a = Move(rx, ry, k)
            # 둘 다 모두 움직이지 않으면 pass
            if step_a == 0 and step_b == 0:
                continue
            # 두 구슬의 위치가 같을 때
            if (arx, ary) == (bbx, bby):
                # 위치가 구멍이라면 파랑구슬이 구멍에 빠져 pass
                if hole[0] == arx and hole[1] == ary:
                    continue
                # 위쪽 방향일 때
                if k == 0:
                    # 빨간 구슬이 더 움직였으면 빨간구슬 한 칸 밑으로
                    if step_a > step_b:
                        arx += 1
                    else:
                        bbx += 1
                # 다른 방향일 때 반복
                elif k == 1:
                    if step_a > step_b:
                        ary -= 1
                    else:
                        bby -= 1
                elif k == 2:
                    if step_a > step_b:
                        arx -= 1
                    else:
                        bbx -= 1
                elif k == 3:
                    if step_a > step_b:
                        ary += 1
                    else:
                        bby += 1
                # 큐에 변경된 위치 추가
                queue.append([arx, ary, bbx, bby, count+1])
            # 빨간 구슬만 구멍에 빠졌을 때
            elif hole[0] == arx and hole[1] == ary:
                return count + 1
            # 파란 구슬만 구멍에 빠졌을 때
            elif hole[0] == bbx and hole[1] == bby:
                continue
            # 큐에 추가
            else:
                queue.append([arx, ary, bbx, bby, count + 1])
    return -1

N, M = map(int, input().split())
arr = [input() for _ in range(N)]
# print(Bead(N, M, arr))
print(Bead(N, M, arr))