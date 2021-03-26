def sqrt(N):
    left = 1
    right = N
    while left <= right:
        mid = (left + right) // 2
        if mid ** 2 < N:
            left = mid + 1
        elif mid ** 2 > N:
            right = mid - 1
        else:
            return mid

N = int(input())
print(sqrt(N))