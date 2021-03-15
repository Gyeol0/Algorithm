def cal(X, count):

    Y = 0
    for s in X:
        Y += int(s)
    if len(X) >= 2:
        count += 1
    if Y < 10:
        if Y % 3 == 0:
            return count, 'YES'
        else:
            return count, 'NO'
    else:
        return cal(str(Y), count)

X = input()
count, result = cal(X, 0)
print(count)
print(result)