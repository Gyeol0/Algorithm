def atm(N, P):
    arr = [i for i in range(N)]
    # 빨리 끝나는 사람부터
    arr = sorted(arr, key = lambda x: P[x])
    answer = 0
    plus = 0
    for i in arr:
        plus += P[i]
        answer += plus
    return answer

N = int(input())
P = list(map(int, input().split()))
print(atm(N, P))