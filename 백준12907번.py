def animal(N, arr):
    '''
    토끼와 고양이 둘 중 하나
    무조건 0부터 연속된 숫자가 있어야함
    한 번에 모두 지워지면 고양이나 토끼 둘 중 하나만

    두 번 지웠는데 남아 있으면 불가능 0
    토끼와 고양이 수가 같으면 2 ** 마리 수
    다르면 (2 ** 작은 마리 수) * 2

    '''
    max_arr = max(arr)
    for i in range(max_arr + 1):
        if i not in arr:
            return 0
        arr.remove(i)
    # 토끼나 고양이 둘 중 하나만 있음
    if not arr:
        return 2
    max_arr2 = max(arr)
    for i in range(max_arr2 + 1):
        if i not in arr:
            return 0
        arr.remove(i)
    if arr:
        return 0
    if max_arr > max_arr2:
        return (2 ** (max_arr2 + 1)) * 2
    else:
        return (2 ** (max_arr2 + 1))

N = int(input())
arr = list(map(int, input().split()))
print(animal(N, arr))