def f(x, y, d1, d2):
    global min_value
    boundary_graph = [[0]*N for _ in range(N)]
    # 경계선 인구
    boundary = 0

    for k in range(d1+1):
        boundary += arr[x+k-1][y-k-1]
        boundary_graph[x+k-1][y-k-1] = 1
    for k in range(d2+1):
        boundary += arr[x+k-1][y+k-1]
        boundary_graph[x+k-1][y+k-1] = 1
    for k in range(d2+1):
        boundary += arr[x+d1+k-1][y-d1+k-1]
        boundary_graph[x+d1+k-1][y-d1+k-1] = 1
    for k in range(d1+1):
        boundary += arr[x+d2+k-1][y+d2-k-1]
        boundary_graph[x+d2+k-1][y+d2-k-1] = 1


    # 중복 제거
    boundary -= arr[x - 1][y - 1]
    boundary -= arr[x+d1-1][y-d1-1]
    boundary -= arr[x+d2-1][y+d2-1]
    boundary -= arr[x+d1+d2-1][y-d1+d2-1]
    # 5번 선거구 채우기
    for i in range(x+1, x+d1+d2):
        start = False
        for j in range(N):
            if boundary_graph[i-1][j] == 1:
                if start:
                    break
                else:
                    start = True
            elif start:
                boundary_graph[i-1][j] = 1

    people = []
    # 1번 선거구
    sum_people = 0
    for r in range(1, x+d1):
        for c in range(1, y+1):
            if not boundary_graph[r-1][c-1]:
                sum_people += arr[r-1][c-1]
    people.append(sum_people)
    sum_people = 0
    # 2번 선거구
    for r in range(1, x+d2+1):
        for c in range(y+1, N+1):
            if not boundary_graph[r - 1][c - 1]:
                sum_people += arr[r-1][c-1]
    people.append(sum_people)
    sum_people = 0
    # 3번 선거구
    for r in range(x + d1, N+1):
        for c in range(1, y-d1+d2):
            if not boundary_graph[r - 1][c - 1]:
                sum_people += arr[r-1][c-1]
    people.append(sum_people)
    sum_people = 0
    # 4번 선거구
    for r in range(x + d2+1, N+1):
        for c in range(y-d1+d2, N+1):
            if not boundary_graph[r - 1][c - 1]:
                sum_people += arr[r-1][c-1]
    people.append(sum_people)

    # 경계선 내부의 5번 인구
    inner = all_people - sum(people) - boundary
    # 5번 선거구 추가
    people.append(inner + boundary)
    min_value = min(min_value, max(people) - min(people))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
min_value = 99999999999
all_people = 0
for i in range(N):
    all_people += sum(arr[i])
for d1 in range(1, N+1):
    for d2 in range(1, N+1):
        for x in range(1, N+1):
            for y in range(1, N+1):
                if 1 <= x < x+d1+d2 <= N and 1 <= y-d1 < y < y+d2 <= N:
                    f(x, y, d1, d2)
print(min_value)