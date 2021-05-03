def sub(N):
    sum_subset = set()
    for i in range(1<<N):
        subset = []
        for j in range(N):
            if i & (1<<j):
                subset.append(arr[j])
        if subset:
            sum_subset.add(sum(subset))
    sum_subset = sorted(sum_subset)
    result = 1
    idx = 0
    while True:
        if idx < len(sum_subset) and sum_subset[idx] == result:
            idx += 1
            result += 1
        else:
            return result

N = int(input())
arr = list(map(int, input().split()))
print(sub(N))

def go(idx, sum_value):
    if idx == N:
        visit[sum_value] = True
        return
    # 현재 포함
    go(idx+1,sum_value+arr[idx])
    # 현재 포함x
    go(idx+1,sum_value)
N = int(input())
arr = list(map(int, input().split()))
visit = [False]*(N*100000+10)
go(0,0)
k= 1
while True:
    if visit[k] == False:
        break
    k += 1
print(k)