def Remote(error, N):
    min_result = abs(N - 100)
    key = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    key = key - error
    # 모든 값 계산
    for i in range(1000001):
        flag = True
        # 버튼을 누를 수 있는지 확인
        for j in str(i):
            if j not in key:
                flag = False
                break
        if flag:
            if len(str(i)) + abs(N-i) < min_result:
                min_result = len(str(i)) + abs(N-i)
    return min_result

N = int(input())
M = int(input())
if M > 0:
    error = set(input().split())
else:
    error = {10}

print(Remote(error, N))
