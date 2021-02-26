from _collections import deque
def solution(arr):
    queue = deque()
    result = []
    for i in arr:
        if i == 'pop':
            if queue:
                print(queue.popleft())
            else:
                print(-1)
        elif i == 'size':
            print(len(queue))
        elif i == 'empty':
            if queue:
                print(0)
            else:
                print(1)
        elif i == 'front':
            if queue:
                print(queue[0])
            else:
                print(-1)
        elif i == 'back':
            if queue:
                print(queue[-1])
            else:
                print(-1)
        else:
            queue.append(int(i.replace('push', '').strip()))

N = int(input())
arr = [input() for _ in range(N)]
solution(arr)
