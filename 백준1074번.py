def Z(n, x, y):
    global count
    if x == r and y == c:
        print(count)
        return

    if n == 1:
        count += 1
        return
    if not (x <= r < x+n and y <= c < y + n):
        count += n*n
        return

    Z(n//2, x, y)
    Z(n//2, x, y + n//2)
    Z(n//2, x + n//2, y)
    Z(n//2, x + n//2, y + n//2)

n, r, c = map(int, input().split())
count = 0
Z(2**n, 0, 0)