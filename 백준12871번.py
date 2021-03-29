"""
최소 공배수를 구해서
같은 길이를 만들어주고 같은지 비교
"""
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def lcm(x,y):
    return (x * y) // gcd(x, y)

def infString(s, t):
    k = lcm(len(s), len(t))
    if s * (k // len(s)) == t * (k // len(t)):
        return 1
    return 0

s = input()
t = input()
print(infString(s, t))