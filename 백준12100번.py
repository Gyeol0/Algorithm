from copy import deepcopy
# from itertools import product
def check(arr):
    value = 0
    for i in range(N):
        for j in range(N):
            value = max(value, arr[i][j][0])
    return value
def move(arr, dir):
    # 왼쪽 이동
    if dir == 1:
        for i in range(N):
            for j in range(1, N):
                k = 1
                while True:
                    if j - k >= 0 and arr[j - k][i][0] != 0:
                        if arr[j - k][i][0] == arr[j][i][0]:
                            if arr[j - k][i][1] == 0 and arr[j][i][1] == 0:
                                arr[j - k][i] = (arr[j - k][i][0] * 2, 1)
                                arr[j][i] = (0, 0)
                                break

                        if arr[j - k][i][0] != arr[j][i][0] or arr[j - k][i][1] == 1 or arr[j][i][1] == 1:
                            if j - k + 1 != j:
                                arr[j - k + 1][i] = (arr[j][i][0], arr[j][i][1])
                                arr[j][i] = (0, 0)
                                break
                            else:
                                break
                    elif j - k < 0:
                        arr[0][i] = (arr[j][i][0], arr[j][i][1])
                        arr[j][i] = (0, 0)
                        break
                    k += 1
    # 아래 이동
    elif dir == 2:
        for i in range(N-1, -1, -1):
            for j in range(N-2, -1, -1):
                k = 1
                while True:
                    if j + k < N and arr[j + k][i][0] != 0:
                        if arr[j + k][i][0] == arr[j][i][0]:
                            if arr[j + k][i][1] == 0 and arr[j][i][1] == 0:
                                arr[j + k][i] = (arr[j + k][i][0] * 2, 1)
                                arr[j][i] = (0, 0)
                                break

                        if arr[j + k][i][0] != arr[j][i][0] or arr[j + k][i][1] == 1 or arr[j][i][1] == 1:
                            if j + k - 1 != j:
                                arr[j + k - 1][i] = (arr[j][i][0], arr[j][i][1])
                                arr[j][i] = (0, 0)
                                break
                            else:
                                break
                    elif j + k >= N:
                        arr[N-1][i] = (arr[j][i][0], arr[j][i][1])
                        arr[j][i] = (0, 0)
                        break
                    k += 1
    # 왼쪽 이동
    elif dir == 3:
        for i in range(N):
            for j in range(1, N):
                k = 1
                while True:
                    if j - k >= 0 and arr[i][j - k][0] != 0:
                        if arr[i][j - k][0] == arr[i][j][0]:
                            if arr[i][j - k][1] == 0 and arr[i][j][1] == 0:
                                arr[i][j - k] = (arr[i][j - k][0] * 2, 1)
                                arr[i][j] = (0, 0)
                                break

                        if arr[i][j - k][0] != arr[i][j][0] or arr[i][j - k][1] == 1 or arr[i][j][1] == 1:
                            if j - k + 1 != j:
                                arr[i][j - k + 1] = (arr[i][j][0], arr[i][j][1])
                                arr[i][j] = (0, 0)
                                break
                            else:
                                break
                    elif j - k < 0:
                        arr[i][0] = (arr[i][j][0], arr[i][j][1])
                        arr[i][j] = (0, 0)
                        break
                    k += 1
    # 오른쪽 이동
    elif dir == 4:
        for i in range(N-1, -1, -1):
            for j in range(N-2, -1, -1):
                k = 1
                while True:
                    if j + k < N and arr[i][j + k][0] != 0:
                        if arr[i][j + k][0] == arr[i][j][0]:
                            if arr[i][j + k][1] == 0 and arr[i][j][1] == 0:
                                arr[i][j + k] = (arr[i][j + k][0] * 2, 1)
                                arr[i][j] = (0, 0)
                                break

                        if arr[i][j + k][0] != arr[i][j][0] or arr[i][j + k][1] == 1 or arr[j][i][1] == 1:
                            if j + k - 1 != j:
                                arr[i][j + k - 1] = (arr[i][j][0], arr[i][j][1])
                                arr[i][j] = (0, 0)
                                break
                            else:
                                break
                    elif j + k >= N:
                        arr[i][N-1] = (arr[i][j][0], arr[i][j][1])
                        arr[i][j] = (0, 0)
                        break
                    k += 1

def game(arr, count):
    global max_num
    # perms = list(product([1, 2, 3, 4], repeat=5))
    # for perm in perms:
    #     arr = deepcopy(arr1)
    #     for i in perm:
    #         move(arr, i)
    #         for p in range(N):
    #             for q in range(N):
    #
    #         max_num = max(max_num, check(arr))

    if count == 5:
        max_num = max(max_num, check(arr))
        return

    for i in range(N):
        for j in range(N):
            arr[i][j] = (arr[i][j][0], 0)

    arr1 = deepcopy(arr)
    for i in range(1, 5):
        move(arr, i)
        game(arr, count + 1)
        arr = deepcopy(arr1)



N = int(input())
arr = [list(zip(map(int, input().split()), [0] * N)) for _ in range(N)]
max_num = 0
game(arr, 0)
print(max_num)
