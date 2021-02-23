def Word_Reverse(word):
    result = ''
    w = ''
    # 태그가 열렸는지
    open = False
    for i in word:
        # 공백일 때
        if i == ' ':
            result += w + i
            w = ''
        else:
            # 태그가 열렸을 때
            if i == '<':
                open = True
            if open:
                w += i
                # 태그가 닫혔을 때
                if i == '>':
                    open = False
                    result += w
                    w = ''
            # 태그가 아닐 때, 역순
            else:
                w = i + w
    # 마지막 단어 추가
    result += w
    return result

print(Word_Reverse(input()))

