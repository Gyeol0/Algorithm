import sys
# i에서 i로가는지 체크
def Check(N, H):
    # 각 사다리마다
    for i in range(N):
        x = -1
        y = i
        # 밑으로 내려감
        while 0 <= x + 1 < H:
            ax = x + 1
            ay = y
            # 사다리 만났을 때
            if arr[ax][ay] != 0:
                # 왼쪽으로 연결된 사다리인지
                if 0 <= ay - 1 and arr[ax][ay - 1] == arr[ax][ay]:
                    y = ay - 1
                # 오른족으로 연결된 사다리인지
                elif ay + 1 < N and arr[ax][ay + 1] == arr[ax][ay]:
                    y = ay + 1
            else:
                y = ay
            x = ax
        ay = y
        # i로 안내려옴
        if ay != i:
            return False
    return True

# 조합, 백트래킹
def Ladder(N, idx, count):
    global c, min_result
    # 현재 최솟값보다 크면 가지치기
    if count >= min_result:
        return
    # i에서 i로 내려가는지 확인
    if Check(N, H):
        min_result = count
        return
    # 사다리를 설치하는 모든 경우의 수
    for i in range(idx, H):
        for j in range(N-1):
            if arr[i][j] == 0 and arr[i][j+1] == 0:
                arr[i][j] = c
                arr[i][j+1] = c
                c += 1
                Ladder(N, i, count + 1)
                # 다시 제거
                arr[i][j] = 0
                arr[i][j+1] = 0
                c -= 1
N, M, H = map(int, sys.stdin.readline().split())
arr = [[0]*N for _ in range(H)]
min_result = 4
c = 1
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    arr[a-1][b-1] = c
    arr[a-1][b] = c
    c += 1
Ladder(N,0,0)
if min_result == 4:
    min_result = -1
print(min_result)
