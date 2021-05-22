def dfs(idx):
    global count
    if idx == 10:
        s = 0
        for j in range(10):
            if my_answer[j] == answer[j]:
                s += 1
        if s >= 5:
            count += 1
        return

    for i in range(1, 6):
        if idx > 1 and my_answer[idx - 2] == my_answer[idx - 1] == i:
            continue
        my_answer.append(i)
        dfs(idx + 1)
        my_answer.pop()


answer = list(map(int, input().split()))
count = 0
my_answer = []
dfs(0)
print(count)