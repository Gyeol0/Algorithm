def prim(start):
    new_graph = [[0] * N for _ in range(N)]
    # 정점마다 거리 계산
    for i in range(N):
        for j in range(N):
            dis = ((graph[i][0] - graph[j][0]) ** 2 + (graph[i][1] - graph[j][1]) ** 2) ** 0.5
            new_graph[i][j] = dis

    # prim
    distance = [INF] * N
    visit = [0] * N
    distance[start] = 0
    for _ in range(N):
        min_value = INF
        # 가장 짧은 거리의 정점 찾기
        for i in range(N):
            if visit[i] == 0 and distance[i] < min_value:
                min_value = distance[i]
                now = i
        visit[now] = 1
        for i in range(N):
            if visit[i] == 0:
                distance[i] = min(distance[i], new_graph[now][i])

    return round(sum(distance), 2)

N = int(input())
graph = [list(map(float, input().split())) for _ in range(N)]
INF = 999999999999999
print(prim(0))