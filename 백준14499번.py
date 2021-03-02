# 1 동, 2 서, 3 북, 4 남
def Dice(x, y, arr, order):
    # 주사위 위, 북, 동, 서, 남, 바닥 순으로
    dice = [0, 0, 0, 0, 0, 0]
    # 이동
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    for i in order:
        ax = x + dx[i-1]
        ay = y + dy[i-1]
        # 범위 넘어가는지 확인
        if 0 <= ax < N and 0 <= ay < M:
            # 명령에 따라 주사위가 굴러가면서 숫자가 바뀜
            if i == 1:
                dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
            elif i == 2:
                dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
            elif i == 3:
                dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
            elif i == 4:
                dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
            # 조건
            if arr[ax][ay] == 0:
                arr[ax][ay] = dice[5]
            else:
                dice[5] = arr[ax][ay]
                arr[ax][ay] = 0
            x = ax
            y = ay
            # 윗면에 있는 숫자 출력
            print(dice[0])

N, M, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
order = list(map(int, input().split()))
Dice(x, y, arr, order)