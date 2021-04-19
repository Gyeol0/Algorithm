def turn(N, M, arr, rotation):
    change = [[0]*(M+1) for _ in range(N+1)]
    # 각 원판마다 총 몇 번 회전했는지 저장
    turn_value = [0]*(N+1)
    for t in range(T):
        x, d, k = rotation[t]
        # 삭제가 일어났는지 확인
        flag = False
        for i in range(1, N+1):
            # 배수인지 확인
            if i % x == 0:
                # 시계 방향 회전
                if d == 0:
                    turn_value[i] -= k
                else:
                    turn_value[i] += k

        for i in range(1, N+1):
            # i번째 원판의 회전 횟수
            a = turn_value[i]
            # 조건 1
            p1 = (1+a)%M
            p2 = (2+a)%M
            p3 = (M+a)%M
            if p1 == 0:
                p1 = M
            if p2 == 0:
                p2 = M
            if p3 == 0:
                p3 = M

            k1 = arr[i][p1]
            if k1 != 'x' and k1 == arr[i][p2]:
                change[i][p1] = 1
                change[i][p2] = 1
            if k1 != 'x' and k1 == arr[i][p3]:
                change[i][p1] = 1
                change[i][p3] = 1
            # 조건 2
            p4 = (M-1+a)%M
            if p4 == 0:
                p4 = M
            k2 = arr[i][p3]
            if k2 != 'x' and k2 == arr[i][p4]:
                change[i][p4] = 1
                change[i][p3] = 1
            if k2 != 'x' and k2 == arr[i][p1]:
                change[i][p1] = 1
                change[i][p3] = 1

            # 조건 3
            for j in range(2, M):
                p5 = (j + a) % M
                p6 = (j - 1 + a) % M
                p7 = (j + 1 + a) % M
                if p5 == 0:
                    p5 = M
                if p6 == 0:
                    p6 = M
                if p7 == 0:
                    p7 = M
                k3 = arr[i][p5]
                if k3 != 'x' and k3 == arr[i][p6]:
                    change[i][p6] = 1
                    change[i][p5] = 1
                if k3 != 'x' and k3 == arr[i][p7]:
                    change[i][p7] = 1
                    change[i][p5] = 1

            # 조건 4, 5, 6
            for j in range(1, M+1):

                p5 = (j + a) % M

                if p5 == 0:
                    p5 = M
                k4 = arr[i][p5]
                # 조건 4
                if i == 1:
                    b = turn_value[2]
                    p5_1 = (j + b) % M
                    if p5_1 == 0:
                        p5_1 = M
                    if k4 != 'x' and k4 == arr[2][p5_1]:
                        change[2][p5_1] = 1
                        change[1][p5] = 1
                # 조건 6
                elif i == N:
                    b = turn_value[N-1]
                    p5_1 = (j + b) % M
                    if p5_1 == 0:
                        p5_1 = M
                    if k4 != 'x' and k4 == arr[N-1][p5_1]:
                        change[N][p5] = 1
                        change[N-1][p5_1] = 1
                # 조건 5
                else:
                    b = turn_value[i-1]
                    c = turn_value[i+1]
                    p5_1 = (j + b) % M
                    p5_2 = (j + c) % M
                    if p5_1 == 0:
                        p5_1 = M
                    if p5_2 == 0:
                        p5_2 = M
                    if k4 != 'x' and k4 == arr[i-1][p5_1]:
                        change[i][p5] = 1
                        change[i-1][p5_1] = 1
                    if k4 != 'x' and k4 == arr[i+1][p5_2]:
                        change[i][p5] = 1
                        change[i+1][p5_2] = 1

        # 바뀐 부분이 있으면 x으로 바꾸고, change 재사용할 수 있게 0으로
        for i in range(1, N+1):
            for j in range(1, M+1):
                if change[i][j] == 1:
                    flag = True
                    arr[i][j] = 'x'
                    change[i][j] = 0

        # 바뀐 부분이 없으면 평균 계산해서 +1, -1
        if not flag:
            total = 0
            count = 0
            for i in range(1, N+1):
                for j in range(1, M+1):
                    if arr[i][j] != 'x':
                        total += arr[i][j]
                        count += 1

            if count != 0:
                average = total / count
                for i in range(1, N+1):
                    for j in range(1, M+1):
                        if arr[i][j] != 'x':
                            if average > arr[i][j]:
                                arr[i][j] += 1
                            elif average < arr[i][j]:
                                arr[i][j] -= 1

            # 모든 숫자가 삭제되어서 모두 x이면 그만
            else:
                break
    result = 0
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j] != 'x':
                result += arr[i][j]
    return result

N, M, T = map(int, input().split())
arr = [[0] * (M+1)]
for _ in range(N):
    arr.append([0] + list(map(int, input().split())))
rotation = [list(map(int, input().split())) for _ in range(T)]
print(turn(N, M, arr, rotation))