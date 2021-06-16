def ageSort(arr):
    arr = sorted(arr, key=lambda x: int(x[0]))
    for i in arr:
        print(i[0], i[1])
N = int(input())
arr = [input().split() for i in range(N)]
ageSort(arr)