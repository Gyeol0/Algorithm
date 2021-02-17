def Add_Bracket(N, exp, i, result):
    # 괄호가 있을 경우와 없을 경우를 모두 구해야 한다.
    # i : 현재 위치
    # result : 현재까지 계산 결과
    global max_result
    # 모든 연산자 수행, 종료
    if i == N:
        max_result = max(max_result, result)
        return
    # 현재 위치에 괄호가 있을 경우
    if exp[i] == '+':
        # N-2가 되면 마지막 연산자
        # 마지막 재귀
        if i == N-2:
            return Add_Bracket(N, exp, i+2, result + int(exp[i+1]))
        Add_Bracket(N, exp, i+2, result + int(exp[i+1]))
        # 현재 위치에 괄호가 없을 경우, 뒤가 먼저 계산
        # 두 연산자를 계산해서 i + 4로 이동
        # 첫 번째 연산자는 +
        if exp[i+2] == '+':
            Add_Bracket(N, exp, i + 4, result + (int(exp[i + 1]) + int(exp[i+3])))
        elif exp[i+2] == '*':
            Add_Bracket(N, exp, i + 4, result + (int(exp[i + 1]) * int(exp[i+3])))
        elif exp[i+2] == '-':
            Add_Bracket(N, exp, i + 4, result + (int(exp[i + 1]) - int(exp[i+3])))
    # 첫 번째 연산자 *
    # +와 동일
    elif exp[i] == '*':
        # N-2가 되면 마지막 연산자
        # 마지막 재귀
        if i == N-2:
            return Add_Bracket(N, exp, i+2, result * int(exp[i+1]))
        Add_Bracket(N, exp, i+2, result * int(exp[i+1]))
        if exp[i+2] == '+':
            Add_Bracket(N, exp, i + 4, result * (int(exp[i + 1]) + int(exp[i+3])))
        elif exp[i+2] == '*':
            Add_Bracket(N, exp, i + 4, result * (int(exp[i + 1]) * int(exp[i+3])))
        elif exp[i+2] == '-':
            Add_Bracket(N, exp, i + 4, result * (int(exp[i + 1]) - int(exp[i+3])))
    # 첫 번째 연산자 -
    elif exp[i] == '-':
        # N-2가 되면 마지막 연산자
        # 마지막 재귀
        if i == N-2:
            return Add_Bracket(N, exp, i+2, result - int(exp[i+1]))
        Add_Bracket(N, exp, i+2, result - int(exp[i+1]))
        if i == N-2:
            return
        if exp[i+2] == '+':
            Add_Bracket(N, exp, i + 4, result - (int(exp[i + 1]) + int(exp[i+3])))
        elif exp[i+2] == '*':
            Add_Bracket(N, exp, i + 4, result - (int(exp[i + 1]) * int(exp[i+3])))
        elif exp[i+2] == '-':
            Add_Bracket(N, exp, i + 4, result - (int(exp[i + 1]) - int(exp[i+3])))

N = int(input())
exp = input()
max_result = -(2**31)
# 초기값, i = 1 첫 번째 연산자, result = exp[0], 처음 맨 앞 숫자
Add_Bracket(N, exp, 1, int(exp[0]))
print(max_result)