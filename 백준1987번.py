def Alphabet(R, C, arr):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    alp = arr[0][0]
    queue = set()
    max_length = 1
    # set으로 중복 경로 제거
    # 최단 경로가 아니라 모든 queue를 확인해야하기 때문에 중복 경로를 모두 확인하면 시간 초과
    queue.add((0, 0, alp))
    while queue:
        # set은 순서 상관없음
        x, y, alp = queue.pop()
        for k in range(4):
            ax = x + dx[k]
            ay = y + dy[k]
            # 갈 수 있는지 확인
            if 0 <= ax < R and 0 <= ay < C:
                # 방문한 곳인지 확인
                if arr[ax][ay] not in alp:
                    queue.add((ax, ay, alp + arr[ax][ay]))
                    # 하나 이동을 더해서 +1
                    max_length = max(max_length, len(alp) + 1)
    return max_length

R, C = map(int, input().split())
arr = []
for _ in range(R):
    arr.append(input())
print(Alphabet(R, C, arr))
