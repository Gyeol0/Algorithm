N = int(input())
arr =[input() for _ in range(N)]
# 중복 제거
arr = list(set(arr))
# 단어길이, 사전 순 정렬
arr = sorted(arr, key = lambda x : (len(x), x))
for i in range(len(arr)):
    print(arr[i])