N, K = list(map(int,input().split()))

li = []
index = -1
print("<",end="")

for i in range(1,N+1,1):
    li.append(i)

while True:
    for _ in range(K):
        index+=1
        if index ==N:
            index = 0

    if len(li)==1:
        print(li[index], end="")
        break

    print(li[index],end=", ")

    li.remove(li[index])
    
    index-=1
    N-=1

print(">",end="")
