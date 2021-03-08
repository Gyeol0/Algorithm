import sys
def Sum_Num(K, arr):
    stack = []
    for i in range(K):
        # 0이면 stack pop
        if arr[i] == 0:
            stack.pop()
        # 0이 아니면 추가
        else:
            stack.append(arr[i])
    # 합 반환
    return sum(stack)

K = int(input())
arr = [int(sys.stdin.readline()) for _ in range(K)]
print(Sum_Num(K, arr))