def VPS(s):
    stack = []
    for i in s:
        # 여는 괄호이면 스택에 추가
        if i == '(':
            stack.append(i)
        # 닫는 괄호이면 pop
        else:
            # 스택이 비어있으면 여는 괄로가 부족하여 잘못되어 있으므로 NO 반환
            # 있으면 pop
            if stack:
                stack.pop()
            else:
                return 'NO'
    # 끝났는데 괄호 남아 있으면 NO 반환
    if stack:
        return 'NO'
    # 정상적으로 끝나면 YES 반환
    return 'YES'

T = int(input())
for t in range(T):
    s = input()
    print(VPS(s))