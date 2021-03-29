def ab(s1, s2):
    # T를 되돌려서 S가 나오는지 확인
    while s2:
        if s2 == s1:
            return 1
        elif s2[-1] == 'A':
            s2.pop()
        elif s2[-1] == 'B':
            s2.pop()
            s2.reverse()
    return 0

s1 = list(input())
s2 = list(input())
print(ab(s1, s2))
