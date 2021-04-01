# def makeNum(count, K):
#     if count == N:
#         if not arr[K]:
#             arr[K] = 1
#         return
#     makeNum(count + 1, K + 1)
#     makeNum(count + 1, K + 5)
#     makeNum(count + 1, K + 10)
#     makeNum(count + 1, K + 50)
#
# N = int(input())
# arr = [0] * (N * 50 + 1)
# makeNum(0, 0)
# print(sum(arr))

# 백트래킹으로는 안된다
def makeNum(N):
    answer = set()
    for i in range(N + 1):
        for j in range(N + 1 - i):
            for k in range(N + 1 - i - j):
                p = N - i - j - k
                value = i  + j * 5 + k * 10 + p * 50
                answer.add(value)
    return len(answer)
N = int(input())
print(makeNum(N))
