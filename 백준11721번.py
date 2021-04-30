def stringPirnt(s):
    idx = 0
    while idx < len(s):
        print(s[idx:idx+10])
        idx += 10

s = input()
stringPirnt(s)