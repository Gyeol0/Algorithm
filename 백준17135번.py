from collections import deque
import copy
def Defence(N, M, D, arr1):
    archer = []
    max_count = 0
    # 왼쪽 적을 먼쩌 쏘기 때문에 우선으로 탐색, 왼 위 오 순으로
    dx = [0, -1, 0]
    dy = [-1, 0, 1]
    # 궁수의 위치 조합
    for i in range(M):
        for j in range(i+1, M):
            for k in range(j+1, M):
                archer.append((i, j, k))
    # 궁수 위치 조합별 max_count 계산
    for ar in archer:
        count = 0
        l = 0
        arr =copy.deepcopy(arr1)
        # N 만큼 적이 밑으로 내려오면 stop
        while l < N:
            result = []
            # 궁수 3명에 대한 최단 거리 적 계산
            for i in range(3):
                queue = deque()
                queue.append((N, ar[i],0))
                t = 1
                while queue and t:
                    x, y, d = queue.popleft()
                    for k in range(3):
                        ax = x + dx[k]
                        ay = y + dy[k]
                        if 0 <= ax < N and 0 <= ay < M:
                            # 처리가 D 이하이면서 적이 있는 곳 탐색
                            if arr[ax][ay] == 1 and d +1 <= D:
                                # 찾으면 stop, 너비 우선 탐색이기 때문에 먼저 찾으면 최단 거리
                                result.append((ax, ay))
                                t = 0
                                break
                            elif d +1 <= D:
                                # 아직 못찾음
                                queue.append((ax, ay, d+1))
                                # 최단 거리가 D보다 크면 탐색 종료
                            if d +1 > D:
                                t = 0
                                break
            # 적 화살 쏘기
            for i in result:
                if arr[i[0]][i[1]] == 1:
                    count += 1
                    arr[i[0]][i[1]] = 0
            # 적을 한 칸씩 밑으로 내리기
            for i in range(N-1, 0, -1):
                arr[i] = arr[i-1][:]
            arr[0] = [0 for _ in range(M)]
            l += 1
        # 최댓값 비교
        max_count = max(max_count, count)
    return max_count

N, M, D = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
print(Defence(N,M,D,arr))