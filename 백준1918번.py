def Postfix_Notation(expression): # 후위 표기법
    stack = []
    result = ''
    priority_in = {
        '(': 0,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        ')': '-'
    }
    priority_out = {
        '(': 3,
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        ')': '-'
    }

    for i in expression:
        # 피연산자는 push
        if i not in priority_in:
            result += i
        else:   # 연산자

            # 스택이 있을 때
            if stack:
                # 닫는 괄호면 여는 괄호가 나올 때까지 pop
                if i == ')':
                    while stack[-1] != '(':
                        result += stack.pop()
                    stack.pop()
                else:
                    # top보다 우선순위가 클 때까지 pop
                    while stack:
                        if priority_in[stack[-1]] < priority_out[i]:
                            stack.append(i)
                            break
                        else:
                            result += stack.pop()
                    # 스택 비어지면 push
                    if not stack:
                        stack.append(i)
            else:   # 스택이 비었을 때
                stack.append(i)
    # 스택에 남아있을 때 모두 pop
    while stack:
        result += stack.pop()
    return result
print(Postfix_Notation(input()))