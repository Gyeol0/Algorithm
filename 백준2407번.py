def comb(n, r):
    i = n
    j = 1
    result = [0] * (r + 1)
    result[0] = 1
    for k in range(1, r+1):
        result[k] = result[k-1] * i // j
        i -= 1
        j += 1
    return result[-1]

n, m = map(int, input().split())
print(comb(n, m))