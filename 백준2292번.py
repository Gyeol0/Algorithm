N=int(input())
count=0
room=1
num=room

while num<N:
    count+=1
    room=6*count
    num+=room
print(count+1)