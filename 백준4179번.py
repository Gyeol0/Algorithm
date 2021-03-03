from _collections import deque
def Fire(R, C, arr):
    queue = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 두 가지 방법이 있다.
    # 1. 불을 먼저 확산 시키는 방법(처음 queue에 먼저 삽입)
    # 2. J 위치를 먼저 삽입하고, J가 움직였을 때, 네 방향으로 한 칸을 더 움직여봐서 불을 만나는지 확인.
    # 불을 만나게 되면 큐에 넣지 않는다.
    # 2번을 할 경우에는 검사를 한 번 더 하기 때문에 조금 더 비효율
    # 2번 풀이는 주석으로
    
    # 불 먼저 큐에 삽입하고, J 위치 삽입
    # fire = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'J':
                start = (i, j, 0)
            elif arr[i][j] == 'F':
                # fire.append((i, j, 'f'))
                queue.append((i, j, 'f'))
    queue.append(start)
    # queue.extend(fire)
    while queue:
        x, y, c = queue.popleft()

        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            # 불이면서 확산 범위 내일 때
            if c == 'f' and 0 <= ax < R and 0 <= ay < C:
                # 확산
                if arr[ax][ay] == 'J' or arr[ax][ay] == '.':
                    arr[ax][ay] = 'F'
                    # 큐에 삽입
                    queue.append((ax, ay, 'f'))
            # J 일때
            elif c != 'f':
                if 0 <= ax < R and 0 <= ay < C:
                    # 움직일 공간
                    if arr[ax][ay] == '.':
                        flag = True
                        # 2번에서 한 칸 더 갔을 때 불과 만나는지 확인
                        # 불을 큐에 먼저 넣어서 확인할 필요 없음
                        # for p in range(4):
                        #     px = ax + dx[p]
                        #     py = ay + dy[p]
                        #     if 0 <= px < R and 0 <= py < C and arr[px][py] == 'F':
                        #         flag = False
                        #         break
                        if flag:
                            arr[ax][ay] = 'J'
                            queue.append((ax, ay, c + 1))
                else:
                    # 밖으로 나감
                    return c + 1
    # 큐가 비어도 나가지 못함
    return 'IMPOSSIBLE'

R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]
print(Fire(R, C, arr))