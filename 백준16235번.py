import sys
def Tree(K, tree):
    if not tree:
        return 0

    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    # tree 3차원 리스트, 안에 나무 나이들 들어있음
    for y in range(K):
        # 봄하고 여름 같이 진행
        for i in range(N):
            for j in range(N):
                # 나무가 있으면
                if tree[i][j]:
                    # 나이별 정렬
                    tree[i][j].sort()
                    # 새로운 나무들
                    new_tree = []
                    die = 0
                    for age in tree[i][j]:
                        # 양분을 먹음
                        if arr[i][j] >= age:
                            arr[i][j] -= age
                            # 새로운 나무
                            new_tree.append(age + 1)
                        else:
                            # 죽으면 양분 추가
                            die += age // 2
                    # 양분 추가
                    arr[i][j] += die
                    tree[i][j] = []
                    # 새로운 나무로 바꿈
                    tree[i][j].extend(new_tree)
        # 가을, 겨울
        for i in range(N):
            for j in range(N):
                # 나무가 있으면
                if tree[i][j]:
                    # 번식이 가능한지 확인
                    for age in tree[i][j]:
                        if age % 5 == 0:
                            for k in range(8):
                                ax = i + dx[k]
                                ay = j + dy[k]
                                # 번식한 곳에 새로운 나무 추가
                                if 0 <= ax < N and 0 <= ay < N:
                                    tree[ax][ay].append(1)
                # 겨울 양분 추가
                arr[i][j] += A[i][j]

    # 전체 돌면서 나무 확인
    result = 0
    for i in range(N):
        for j in range(N):
            result += len(tree[i][j])

    return result

N, M, K = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

years = 0
arr = [[5]*N for _ in range(N)]
tree = [[[] for _ in range(N)] for _  in range(N)]
for _ in range(M):
    x, y, age = map(int, sys.stdin.readline().split())
    tree[x-1][y-1].append(age)

result = Tree(K, tree)
print(result)