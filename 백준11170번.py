def count(N, M):
    cnt = 0
    for i in range(N, M+1):
        s = str(i)
        for j in s:
            if j == '0':
                cnt += 1
    return cnt

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    print(count(N, M))