def Robot(N, M, robot, arr):
    # 방향이 d일 때 왼쪽 방향 이동
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    # 방향이 d일 때 후진 이동
    back_x = [1, 0, -1, 0]
    back_y = [0, -1, 0, 1]
    # 초기값
    x = robot[0]
    y = robot[1]
    d = robot[2]
    turn = 0
    count = 0
    # 로봇이 있는 곳은 항상 빈 칸
    arr[x][y] = 2
    count += 1
    while True:
        ax = x + dx[d]
        ay = y + dy[d]
        # 청소를 할 수 있는지 확인
        if 0 <= ax < N and 0 <= ay < M:
            if arr[ax][ay] == 0:
                arr[ax][ay] = 2
                count += 1
                # 방향 변경
                d = (d - 1) % 4
                x = ax
                y = ay
                turn = 0
            # 청소 할 수 없어서 방향만 변경
            else:
                d = (d - 1) % 4
                turn += 1
        # 범위를 넘어가서 방향만 변경
        else:
            d = (d - 1) % 4
            turn += 1
        # 네 방향 다 점검했는데 못가서 후진 시도
        if turn == 4:
            ax = x + back_x[d]
            ay = y + back_y[d]
            # 후진이 가능한지 확인
            if 0 <= ax < N and 0 <= ay < M:
                # 후진하고 다시 시도
                if arr[ax][ay] == 2:
                    x = ax
                    y = ay
                    turn = 0
                # 후진 불가, 청소 종료
                else:
                    return count
            # 후진 불가, 청소 종료
            else:
                return count

N , M = map(int, input().split())
robot = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
print(Robot(N, M, robot, arr))