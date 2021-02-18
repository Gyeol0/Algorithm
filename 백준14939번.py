import copy
# 켜져 있는 전구는 끄고, 꺼져 있는 전구는 킨다.
def swap(p):
    if p == '#':
        return 'O'
    else:
        return '#'
def fire(arr):
    min_count = 999
    dx = [1, -1, 0, 0, 0]
    dy = [0, 0, 1, -1, 0]
    # 바로 위에 있는 전구가 켜져 있는지 확인이 필요
    # 그런데 맨 윗줄은 벽으로 막혀 있으므로, 모든 경우의 수를 확인해봐야한다.
    # 비트 마스킹으로 10개의 부분집합을 구해, 모든 경우의 수를 찾는다.
    for p in range(1 << 10):
        count = 0
        arr1 = copy.deepcopy(arr)
        for q in range(10):
            if p & (1 << q):
                count += 1
                for r in range(5):
                    ax = 0 + dx[r]
                    ay = q + dy[r]
                    if 0 <= ax < 10 and 0 <= ay < 10:
                        arr1[ax][ay] = swap(arr1[ax][ay])
        # 바로 위에 있는 전구가 켜져 있으면 지나가면서 스위치를 누른다.
        for i in range(10):
            for j in range(10):
                if i != 0:
                    if arr1[i-1][j] == 'O':
                        count += 1
                        for k in range(5):
                            ax = i + dx[k]
                            ay = j + dy[k]
                            if 0 <= ax < 10 and 0 <= ay < 10:
                                arr1[ax][ay] = swap(arr1[ax][ay])
        solution = True
        for i in range(10):
            if arr1[9][i] == 'O':
                count = -1
                solution = False
        if solution:
            min_count = min(min_count, count)
    if min_count != 999:
        return min_count
    else:
        return -1
arr = []
for _ in range(10):
    arr.append(list(input()))
print(fire(arr))

