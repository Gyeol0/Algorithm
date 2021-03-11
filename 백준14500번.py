# 완전 탐색 풀이
def tetro(N, M, arr):
    answer = 0
    # 테크노미노의 모든 경우의 수 19가지
    t = [
        [(0, 1), (0, 2), (0, 3)], [(1, 0), (2, 0), (3, 0)], # 1번
        [(0, 1), (1, 0), (1, 1)], # 2번
        [(1, 0), (2, 0), (2, 1)], [(1, 0), (2, 0), (2, -1)], [(0, 1), (0, 2), (-1, 2)],
        [(0, 1), (0, 2), (1, 2)], [(1, 0), (1, 1), (1, 2)], [(1, 0), (0, 1), (0, 2)],
        [(0, 1), (1, 1), (2, 1)], [(0, 1), (1, 0), (2, 0)], # 3번
        [(1, 0), (1, 1), (2, 1)], [(1, 0), (0, 1), (-1, 1)], [(0, 1), (-1, 1), (-1, 2)], [(0, 1), (1, 1), (1, 2)], # 4번
        [(0, 1), (0, 2), (1, 1)], [(0, 1), (0, 2), (-1, 1)], [(0, 1), (-1, 1), (1, 1)], [(-1, 0), (1, 0), (0, 1)] # 5번
    ]

    # 모든 경우 비교
    for i in range(N):
        for j in range(M):
            for te in t:
                result = 0
                result += arr[i][j]
                for k in range(3):
                    ax = i + te[k][0]
                    ay = j + te[k][1]
                    if 0 <= ax < N and 0 <= ay < M:
                        result += arr[ax][ay]
                    else:
                        break
                    if k == 2:
                        answer = max(answer, result)
    return answer

# 백트래킹 풀이
# 남은 개수를 모두 최댓값으로 채워도 더 작으면 가지치기
def tetro2(x, y, count, value):
    global max_value, result

    # 가지치기
    if (4 - count) * max_value + value <= result:
        return
    if count == 4:
        result = max(value, max_value)
        return

    for k in range(4):
        ax = x + dx[k]
        ay = y + dy[k]
        if 0 <= ax < N and 0 <= ay < M and not visit[ax][ay]:
            # ㅗ 모양
            if count == 2:
                visit[ax][ay] = 1
                tetro2(x, y, count + 1, value + arr[ax][ay])
                visit[ax][ay] = 0
            visit[ax][ay] = 1
            tetro2(ax, ay, count + 1, value + arr[ax][ay])
            visit[ax][ay] = 0

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
visit = [[0]*M for _ in range(N)]
max_value = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(N):
    max_value = max(max_value, max(arr[i]))
for i in range(N):
    for j in range(M):
        visit[i][j] = 1
        tetro2(i, j, 1, arr[i][j])
        visit[i][j] = 0
print(result)