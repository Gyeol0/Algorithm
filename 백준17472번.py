from collections import deque
from itertools import combinations
def swap(a,b):
    if a > b:
        return (b, a)
    else:
        return (a, b)
def Bridge(N, M, arr):
    queue = deque()
    dx = [1, -1, 0, 0, 0]
    dy = [0, 0, 1, -1, 0]
    island = 2
    # 섬 라벨링
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1:
                queue.append([i, j])
                arr[i][j] = island
                while queue:
                    x, y = queue.popleft()
                    for k in range(4):
                        ax = x + dx[k]
                        ay = y + dy[k]
                        if 0 <= ax < N and 0 <= ay < M:
                            if arr[ax][ay] == 1:
                                arr[ax][ay] = island
                                queue.append([ax,ay])
                island += 1
    arr_visit = [[0]*M for _ in range(N)]
    passing = []
    visit ={}
    for i in range(2, island):
        visit[i] = {}
    # 섬마다 최단 거리 만들기(다리)
    for i in range(N):
        for j in range(M):
            # 섬 하나 잡아서
            if arr[i][j] != 0 and arr[i][j] not in passing:
                passing.append(arr[i][j])
                queue = deque()
                queue.append([i,j])
                # 섬 내부에서 최단 거리로 갈 수 있는 섬들 탐색
                while queue:
                    x, y = queue.popleft()
                    for k in range(5):
                        ax = x + dx[k]
                        ay = y + dy[k]
                        if 0 <= ax < N and 0 <= ay < M and arr[ax][ay] == arr[i][j]:
                            if arr_visit[ax][ay] == 0:
                                arr_visit[ax][ay] = 1
                                queue.append([ax,ay])
                                queue_1 = deque()
                                for p in range(4):
                                    queue_1.append([ax, ay, p, 0])
                                while queue_1:
                                    xx, yy, d, count = queue_1.popleft()
                                    px = xx + dx[d]
                                    py = yy + dy[d]
                                    if 0 <= px < N and 0 <= py <M:
                                        if arr[px][py] == 0:
                                            queue_1.append([px, py, d, count + 1])
                                        elif arr[px][py] != arr[i][j]:
                                            # 거리가 2 이상이면서 최단 거리에 있느 섬들 추가
                                            if count >= 2:
                                                if arr[px][py] not in visit[arr[i][j]]:
                                                    visit[arr[i][j]][arr[px][py]] = count
                                                else:
                                                    visit[arr[i][j]][arr[px][py]] = min(visit[arr[i][j]][arr[px][py]], count)
    answer = []
    line = set()
    for i in list(visit.keys()):
        for j in list(visit[i].keys()):
            line.add(swap(i,j))
    line = list(line)
    # 다리가 섬-1 보다 작으면 불가능
    if len(line) < island -3:
        return -1
    # 다리가 1이면 바로 출력
    elif len(line) == 1:
        return visit[line[0][0]][line[0][1]]
    com = list(combinations(line, island -3))
    # 섬-1 개의 다리를 조합으로 선택하여 최솟값 출력
    for i in com:
        search = set()
        result = 0
        stop = False
        # 모든 섬들이 이어지는지 확인
        for p in range(len(i)):
            check = set()
            for q in range(len(i)):
                if p != q:
                    check.add(i[q][0])
                    check.add(i[q][1])
            if i[p][0] not in check and i[p][1] not in check:
                stop =True
                break
        if stop:
            continue
        # 최단 거리 계산
        for j in i:
            result += visit[j[0]][j[1]]
            search.add(j[0])
            search.add(j[1])
        if len(search) == island -2:
            answer.append(result)
    if answer:
        return min(answer)
    else:
        return -1

N, M = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
print(Bridge(N, M, arr))