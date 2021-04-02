def is_Circular(s):
    if s == s[::-1]:
        return 0
    count1 = 0
    count2 = 0
    left1 = 0
    left2 = 0
    right1 = len(s) - 1
    right2 = len(s) - 1
    while left1 < right1:
        if s[left1] != s[right1]:
            count1 += 1
            left1 += 1
        else:
            left1 += 1
            right1 -= 1

    while left2 < right2:
        if s[left2] != s[right2]:
            count2 += 1
            right2 -= 1
        else:
            left2 += 1
            right2 -= 1
    if count1 == 1 or count2 == 1:
        return 1
    return 2
T = int(input())
for t in range(T):
    s = input()
    print(is_Circular(s))
