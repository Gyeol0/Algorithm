from _collections import deque
import sys
def solution(p):
    global queue
    if p[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif p[0] == 'size':
        print(len(queue))
    elif p[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif p[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif p[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
    else:
        queue.append(p[1])

N = int(sys.stdin.readline())
queue = deque()
for _ in range(N):
    p = sys.stdin.readline().split()
    solution(p)