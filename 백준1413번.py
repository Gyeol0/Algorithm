def serialSum(s):
    result = 0
    for i in s:
        if i.isdigit():
            result += int(i)
    return result

N = int(input())
arr = [input() for _ in range(N)]
arr = sorted(arr, key=lambda x: (len(x), serialSum(x), x))
for i in arr:
    print(i)