# 최대 공약수
def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# 최소 공배수
def lcm(x, y):
    return (x*y) // gcd(x, y)

x, y = map(int, input().split())
print(gcd(x, y))
print(lcm(x, y))