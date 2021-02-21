from itertools import permutations
import copy
def Turn_Arr(N, M, arr1, K, cal):
    # 초기값
    min_result = 99999999999
    # 돌릴 순서 오른쪽, 아래, 왼쪽, 위 시계 방향
    dx = [0, 1, 0,-1]
    dy = [1, 0, -1, 0]
    # 모든 순서 경우의 수 
    for per in permutations(cal, K):
        arr = copy.deepcopy(arr1)
        for i in list(per):
            r, c, s = i[0], i[1], i[2]
            # 왼쪽 위
            start = [r-s-1, c-s-1]
            # 오른쪽 아래
            end = [r+s-1, c+s-1]
            # 중앙
            mid = [(start[0] + end[0]) // 2, (start[1] + end[1]) // 2]
            x = start[0]
            y = start[1]
            # 중앙에 오기 전까지 돌리기
            while x < mid[0] and y < mid[1]:
                x = start[0]
                y = start[1]
                k = 0
                # 현재 값 저장
                current = arr[x][y]
                while k < 4:
                    ax = x + dx[k]
                    ay = y + dy[k]
                    if start[0] <= ax <= end[0] and start[1] <= ay <= end[1]:
                        arr[ax][ay], current = current, arr[ax][ay]
                        x = ax
                        y = ay
                    else:
                        k += 1
                # 안으로 들어가면서 왼쪽 위, 오른쪽 아래 축소
                start[0] += 1
                start[1] += 1
                end[0] -= 1
                end[1] -= 1
        for i in range(N):
            min_result = min(sum(arr[i]), min_result)
    return min_result

N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
cal = [tuple(map(int, input().split())) for _ in range(K)]
print(Turn_Arr(N, M, arr, K, cal))