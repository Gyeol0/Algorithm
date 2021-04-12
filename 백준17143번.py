def fishing(M, fish, arr):
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, 1, -1]
    result = 0
    for p in range(C):
        # 이동하면서 고기를 잡는다
        for q in range(R):
            if arr[q][p]:
                result += arr[q][p][2]
                arr[q][p] = 0
                break
        # 고기를 새로 리스트에 담아준다.
        fish = []
        for r in range(R):
            for c in range(C):
                if arr[r][c]:
                    fish.append((r + 1, c + 1, arr[r][c][0], arr[r][c][1], arr[r][c][2]))
                    arr[r][c] = 0

        # 상어 이동
        l = len(fish)
        for i in range(l):
            x = fish[i][0]
            y = fish[i][1]
            arr[x-1][y-1] = 0
            speed = fish[i][2]
            dir = fish[i][3]
            weight = fish[i][4]
            # 방향에 따라 이동
            ax = x + dx[dir] * speed
            ay = y + dy[dir] * speed
            # 범위를 넘어가지 않으면 바로 이동
            if 0 <= ax - 1 < R and 0 <= ay - 1 < C:
                fish[i] = (ax, ay, speed, dir, weight)
    
            else:
                # 넘어가면 방향에 따라 구분
                # (가로 or 세로 칸 - 1) * 2 마다 반복
                if dir == 1:
                    go = speed % ((R - 1) * 2)
                    # 현재 앞에 남은 칸보다 가야할 칸이 더 많으면 방향을 최소 한 번 바꿔야 한다.
                    if x -1 < go:
                        dir = 2
                        x = go - (x-1) + 1
                        # 한 번 바꿨는데도 넘어가면 한 번 더 바꿔야 한다.
                        if x > R:
                            dir = 1
                            x = R - (x - R)
                    else:
                        x -= go
    
                elif dir == 2:
                    go = speed % ((R - 1) * 2)
                    if R - x < go:
                        dir = 1
                        x = R - (go - (R - x))
                        if x < 1:
                            dir = 2
                            x = 1 + 1 - x
                    else:
                        x += go
    
                elif dir == 3:
                    go = speed % ((C - 1) * 2)
                    if C - y < go:
                        dir = 4
                        y = C - (go - (C - y))
                        if y < 1:
                            dir = 3
                            y = 1 + 1 - y
                    else:
                        y += go

                elif dir == 4:
                    go = speed % ((C - 1) * 2)
                    if y - 1 < go:
                        dir = 3
                        y = go - (y - 1) + 1
                        if y > C:
                            dir = 4
                            y = C - (y - C)
                    else:
                        y -= go
                # 이동한 고기를 다시 리스트에 넣어준다.
                fish[i] = (x, y, speed, dir, weight)

        # 고기를 arr에 올려두면서 위치가 겹치면 덩치가 큰 놈들로 교체
        for i in range(l):
            x = fish[i][0] - 1
            y = fish[i][1] - 1
            if arr[x][y]:
                if arr[x][y][2] < fish[i][4]:
                    arr[x][y] = (fish[i][2], fish[i][3], fish[i][4])
            else:
                arr[x][y] = (fish[i][2], fish[i][3], fish[i][4])

    return result

R, C, M = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(M)]
arr = [[0]*C for _ in range(R)]
# 처음 상어 올려두기
for i in fish:
    x = i[0] - 1
    y = i[1] - 1
    arr[x][y] = (i[2], i[3], i[4])
print(fishing(M, fish, arr))

                

