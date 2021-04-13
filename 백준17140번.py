def cal(r, c, k, arr):
    R = 3
    C = 3
    count = 0
    try:
        if arr[r - 1][c - 1] == k:
            return count
    except:
        pass

    while count < 100:
        max_R = 0
        max_C = 0
        count += 1
        # R 연산
        if R >= C:
            for i in range(R):
                new_row = []
                value = {}
                for j in range(len(arr[i])):
                    if arr[i][j] not in value and arr[i][j] != 0:
                        value[arr[i][j]] = 1
                    elif arr[i][j] != 0:
                        value[arr[i][j]] += 1
                # 정렬
                value_sort = sorted(value, key=lambda x: (value[x], x))
                for j in value_sort:
                    new_row.append(j)
                    new_row.append(value[j])
                arr[i] = new_row
                max_R = max(max_R, len(new_row))

            # 0 채우기
            for i in range(R):
                while len(arr[i]) < max_R:
                    arr[i].append(0)
        # C 연산
        else:
            # 행열 바꿔서 계산하고 다시 바꾸기
            arr = list(map(list, zip(*arr)))
            for i in range(C):
                new_row = []
                value = {}
                for j in range(len(arr[i])):
                    if arr[i][j] not in value and arr[i][j] != 0:
                        value[arr[i][j]] = 1
                    elif arr[i][j] != 0:
                        value[arr[i][j]] += 1
                value_sort = sorted(value, key=lambda x: (value[x], x))
                for j in value_sort:
                    new_row.append(j)
                    new_row.append(value[j])
                arr[i] = new_row
                max_C = max(max_C, len(new_row))
            # 0 채우기
            for i in range(C):
                while len(arr[i]) < max_C:
                    arr[i].append(0)
            arr = list(map(list, zip(*arr)))

        R = len(arr)
        C = len(arr[0])
        # 범위 나갈 수 있어서 try로
        try:
            if arr[r-1][c-1] == k:
                return count
        except:
            pass

    return -1
r, c, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]
print(cal(r, c, k, arr))