def dfs(idx, num, check):
    global cnt, answer
    # n보다 큰 경우 확인할 버림
    if num > N:
        return

    if N == num:
        cnt += 1
        # k번째 찾으면
        if cnt == k:
            answer = ''.join(check)[:-1]
            return

    # 숫자 바꿔주면서 넣어주기
    for i in range(1, 4):
        check.append(str(i) + '+')
        dfs(idx + 1, num + i, check)
        check.pop()

N, k = map(int, input().split())
cnt = 0
answer = ''
dfs(0, 0, [])
if answer:
    print(answer)
else:
    print(-1)