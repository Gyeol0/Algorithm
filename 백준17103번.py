T = int(input())
nums = [int(input()) for _ in range(T)]
max_num = max(nums)

prime = [False, False] + [True] * (max_num - 1)
# 에라토스테네스의 체, 소수 만들기
for i in range(2, int(max_num ** 0.5) + 1):
    if prime[i]:
        for j in range(2*i, max_num + 1, i):
            if prime[j]:
                prime[j] = False

for num in nums:
    count = 0
    for i in range((num // 2) + 1):
        if prime[i] and prime[num - i]:
            count += 1
    print(count)