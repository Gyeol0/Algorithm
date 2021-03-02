def Cogwheel(wheel, order):
    result = 0
    # 명령에 따라
    for i, j in order:
        # 오른쪽 인접 톱니
        right = i
        # 왼쪽 인접
        left = i -2
        # 톱니 번호와 회전
        turn = {i-1 : j}
        # 오른쪽으로 가면서 회전할 톱니 추가
        while right < 4:
            if wheel[right-1][2] != wheel[right][6]:
                turn[right] = turn[right-1] * (-1)
                right += 1
            else:
                break
        # 왼쪽으로 가면서 회전할 톱니 추가
        while left >= 0:
            if wheel[left+1][6] != wheel[left][2]:
                turn[left] = turn[left+1] * (-1)
                left -= 1
            else:
                break
        # 톱니 회전
        for p, q in turn.items():
            if q == 1:
                # 미리 저장
                new = wheel[p][7]
                # 오른쪽으로 shift
                for k in range(7, 0, -1):
                    wheel[p][k] = wheel[p][k-1]
                wheel[p][0] = new
            else:
                new = wheel[p][0]
                # 왼쪽으로 shift
                for k in range(7):
                    wheel[p][k] = wheel[p][k+1]
                wheel[p][7] = new
    # 점수 계산
    if wheel[0][0] == '1':
        result += 1
    if wheel[1][0] == '1':
        result += 2
    if wheel[2][0] == '1':
        result += 4
    if wheel[3][0] == '1':
        result += 8
    return result

wheel = [list(input()) for _ in range(4)]
N = int(input())
order = [list(map(int, input().split())) for _ in range(N)]
print(Cogwheel(wheel, order))