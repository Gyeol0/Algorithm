def ab(A, count):
    # dfs 백트래킹
    global min_count
    if A == B:
        min_count = min(count, min_count)
        return
    if count >= min_count:
        return
    if A > B:
        return
    ab(A*2, count + 1)
    ab(int(str(A) + '1'), count + 1)

A, B = map(int, input().split())
min_count = 9999999999
ab(A, 0)
if min_count == 9999999999:
    print(-1)
else:
    print(min_count + 1)