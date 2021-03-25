def gcd(x, y):
    while y:
        x, y = y, x % y
    return x
def solution(s):
    s = s.split(':')
    x = gcd(int(s[0]), int(s[1]))
    answer = str(int(s[0]) // x) + ':' + str(int(s[1]) // x)

    return answer

s = input()
print(solution(s))