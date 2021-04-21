from collections import deque
def bfs(N, K):
    queue =deque()
    queue.append((N,0))
    while queue:
        x, count = queue.popleft()
        visit[x] = 1
        # 만나면 stop
        if x == K:
            return count
        # count 증가 안해서 맨 앞으로 보냄
        if x * 2 < 100001 and visit[x*2] == 0:
            queue.insert(0, (x*2, count))
        # -1, +1 이동 큐에 추가
        if x - 1 >= 0 and visit[x-1] == 0:
            queue.append((x-1, count+1))
        if x + 1 < 100001 and visit[x+1] == 0:
            queue.append((x+1, count+1))
N, K = map(int, input().split())
visit = [0] * 100001
print(bfs(N, K))