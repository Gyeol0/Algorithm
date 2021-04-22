def curve(y, x, d, g):
    dragon = []
    dragon.append((x, y, d))
    if d == 0:
        dragon.append((x, y+1, d))
    elif d == 1:
        dragon.append((x-1, y, d))
    elif d == 2:
        dragon.append((x, y-1, d))
    elif d == 3:
        dragon.append((x+1, y, d))
    while g > 0:
        ax = dragon[-1][0]
        ay = dragon[-1][1]
        for i in range(len(dragon)-1, 0, -1):
            d = dragon[i][2]
            if d == 0:
                ax -= 1
                d = 1
            elif d == 1:
                ay -= 1
                d = 2
            elif d == 2:
                ax += 1
                d = 3
            elif d == 3:
                ay += 1
                d = 0
            dragon.append((ax, ay, d))
        g -= 1
    return dragon

N = int(input())
total = []
arr = [[0] * 101 for _ in range(101)]
count = 0
for _ in range(N):
    x, y, d, g = map(int, input().split())
    dragon = curve(x, y, d, g)
    for x, y, d in dragon:
        arr[x][y] = 1
for i in range(100):
    for j in range(100):
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            count += 1
print(count)