from collections import deque
def ac(p, arr):
    count = 0
    answer = ''
    for i in p:
        if i == 'R':
            count += 1
        else:
            if arr:
                if count % 2:
                    arr.pop()
                else:
                    arr.popleft()
            else:
                return 'error'

    if count % 2:
        arr.reverse()
    answer = '[' +','.join(arr) + ']'
    return answer

T = int(input())
for t in range(T):
    p = input()
    N = int(input())
    arr = input()
    arr = arr.strip('[')
    arr = arr.strip(']')
    if arr == '':
        arr = deque()
    else:
        arr = arr.split(',')
        arr = deque(arr)
    print(ac(p, arr))