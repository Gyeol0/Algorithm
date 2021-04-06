def simu(R, C, T, arr):
    count = [[0] * C for _ in range(R)]
    diffusion = [[0] * C for _ in range(R)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 공기청정기 위치
    pure = []
    for i in range(R):
        if arr[i][0] == -1:
            pure.append((i, 0))
    # t초
    for t in range(T):
        # 확산 배열과 확산 개수 배열 생성
        for i in range(R):
            for j in range(C):
                if arr[i][j] == -1:
                    continue
                cnt = 0
                for k in range(4):
                    ax = i + dx[k]
                    ay = j + dy[k]
                    if 0 <= ax < R and 0 <= ay < C and arr[ax][ay] != -1:
                        cnt += 1
                        diffusion[ax][ay] += arr[i][j] // 5
                count[i][j] = cnt

        # 확산
        for i in range(R):
            for j in range(C):
                if arr[i][j] == -1:
                    continue
                arr[i][j] -= (arr[i][j] // 5) * count[i][j]
                # 확산 후 개수 초기화
                count[i][j] = 0
                arr[i][j] += diffusion[i][j]
                # 확산 배열 초기화
                diffusion[i][j] = 0

        # 공기청정기 작동
        # 위쪽
        dx_top = [0, -1, 0, 1]
        dy_top = [1, 0, -1, 0]
        x = pure[0][0]
        y = pure[0][1] + 1
        k = 0
        current = 0
        while True:
            # 한 칸씩 밀리기 때문에 저장해두고 swap
            arr[x][y], current = current, arr[x][y]
            x += dx_top[k]
            y += dy_top[k]
            # 칸 넘어가면 방향 바꿔서
            if x < 0 or x >= R or y < 0 or y >= C:
                x -= dx_top[k]
                y -= dy_top[k]
                k += 1
                x += dx_top[k]
                y += dy_top[k]
                # 공기 청정기 만나면 stop
                if arr[x][y] == -1:
                    break
            else:
                if arr[x][y] == -1:
                    break

        # 아래
        dx_bot = [0, 1, 0, -1]
        dy_bot = [1, 0, -1, 0]
        x = pure[1][0]
        y = pure[1][1] + 1
        k = 0
        current = 0
        while True:
            arr[x][y], current = current, arr[x][y]
            x += dx_bot[k]
            y += dy_bot[k]
            if x < 0 or x >= R or y < 0 or y >= C:
                x -= dx_bot[k]
                y -= dy_bot[k]
                k += 1
                x += dx_bot[k]
                y += dy_bot[k]
                if arr[x][y] == -1:
                    break
            else:
                if arr[x][y] == -1:
                    break
    answer = 0
    for i in range(R):
        answer += sum(arr[i])
    # 공기 청정기 -1 2개
    answer += 2
    return answer


R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
print(simu(R, C, T, arr))