from collections import deque
import sys
def Min_Num(N, L, arr):
    w = deque()
    D = [0 for _ in range(N)]
    for i in range(N):
        # 현재 값보다 값이 크면 pop하면서 작은 것이 나올 때까지
        # 현재 값이 더 크면 그냥 넘어가서 뒤에 append
        # 마지막 값과 비교하기 때문에 w는 정렬되어 있다.
        while w and w[-1][1] > arr[i]:
            w.pop()

        # i - L + 1부터 시작이므로 가장 작고 앞에 값부터 확인
        # i가 0부터니까 i - L 부터
        # 범위 안에 들어가려면 index가 i - L보다 커야함
        # 작거나 같을 때에는 왼쪽값 계속 pop
        while w and i - L >= w[0][0]:
            w.popleft()

        # w가 비었거나 범위안에 들면서 현재값이 최솟값보다 크다.
        w.append((i, arr[i]))

        # 가장 앞의 값이 최솟값
        D[i] = w[0][1]
    return D

N, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(*Min_Num(N, L, arr))