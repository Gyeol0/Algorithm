def promising(idx):
    # 현재까지 만들어진 col에 대해 조건 검사
    for i in range(idx):
        # 조건 1. 같은 열에 있으면 안됨
        # 조건 2. 대각선 상에 있으면 안됨
        if col[idx] == col[i] or abs(col[idx] - col[i]) == idx - i:
            return False
    return True

def dfs(idx):
    global count
    if idx == N:
        count += 1
        return

    for i in range(N):
        col[idx] = i
        if promising(idx):
            dfs(idx+1)

count = 0
N = int(input())
# col[i] 는 i번째 열에는 몇 번째 행에 queen이 있는지
col = [0] * N
dfs(0)
print(count)