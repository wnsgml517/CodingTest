N = int(input())

result = []

r = []

for i in range(0,N):
    n  = list(map(int,input().split()))
    result.append(n)

    
for index, value in enumerate(result):

    cnt = 0
    for i, v in enumerate(result):
        if i==index:
            continue
        if value[0] < v[0] and value[1] < v[1]:
            cnt+=1
    r.append(cnt+1)

for i in r:
    print(i,end=" ")