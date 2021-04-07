from itertools import combinations
from collections import deque
from copy import deepcopy
def bfs(N, M, arr):
    min_time = 99999999
    room_count = 0 # 감염될 공간 개수
    birus = [] # 바이러스 위치를 담을 리스트
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    # 바이러스 리스트에 담기, 공간 개수 카운트
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                birus.append((i, j))
            if arr[i][j] == 0:
                room_count += 1
    # M개 만큼 뽑는 조합 생성
    com = list(combinations(range(len(birus)), M))
    for c in com:
        queue = deque()
        new_arr = deepcopy(arr)
        # 활성화된 바이러스는 3으로 바꾸고 4 시간 큐어 추가
        for i in c:
            x = birus[i][0]
            y = birus[i][1]
            queue.append((x, y, 4))
            new_arr[x][y] = 3
            count = 0
        # bfs
        while queue:
            x, y, time = queue.popleft()
            # 현재 최소 시간보다 크면 그만
            if time - 3 > min_time:
                break
            for k in range(4):
                ax = x + dx[k]
                ay = y + dy[k]
                if 0 <= ax < N and 0 <= ay < N:
                    # 빈 공간일 때
                    if new_arr[ax][ay] == 0:
                        count += 1
                        new_arr[ax][ay] = time
                        queue.append((ax, ay, time + 1))
                    # 비활성 바이러스로 갈 때
                    elif new_arr[ax][ay] == 2:
                        # 감염될 남은 공간이 없으면 그만해도 된다.
                        if count < room_count:
                            new_arr[ax][ay] = time
                            queue.append((ax, ay, time + 1))
                        else:
                            break
        # 하나라도 0이 있으면 실패
        flag = True
        for i in range(N):
            if min(new_arr[i]) == 0:
                flag = False
                break
        # 걸린 시간과 현재 최소 시간 비교
        if flag:
            time = 0
            for i in range(N):
                time = max(max(new_arr[i]), time)
            min_time = min(min_time, time - 3)
    # 변화 없으면 모두 실패
    if min_time == 99999999:
        return -1
    return min_time

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
print(bfs(N, M, arr))