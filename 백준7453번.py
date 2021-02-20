def Sum_Zero(A, B, C, D):
    # (A+B)에 -(C+D)가 있는지 확인
    # 이분탐색으로 찾아야할 것 같은데 이렇게도 풀린다.
    # 뭔가 이상한 문제 같다
    AB = {}
    count = 0
    # A + B 생성
    for i in A:
        for j in B:
            AB[i+j] = AB.get(i+j, 0) + 1

    # A + B에 -(C + D)가 있는지 확인
    for i in C:
        for j in D:
            count += AB.get(-(i+j),0)
    return count

N=int(input())
A=[]
B=[]
C=[]
D=[]
for _ in range(N):
    a, b, c, d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
print(Sum_Zero(A, B, C, D))