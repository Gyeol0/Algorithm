import heapq as hq
import sys
def Max_heap(heap, n):
    if n == 0:
        if heap:
            print(hq.heappop(heap)[1])
        else:
            print(0)
    else:
        hq.heappush(heap, (-n, n))

N = int(input())
heap = []
for _ in range(N):
    n = int(sys.stdin.readline())
    Max_heap(heap, n)