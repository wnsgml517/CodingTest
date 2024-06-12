import sys

N = int(sys.stdin.readline())

max_karo = 0
max_sero = 0


result = []

for i in range(N):
    N = list(map(int,sys.stdin.readline().split()))
    result.append(N)
    
    max_karo = max(max_karo,N[0])
    max_sero = max(max_sero,N[1])


arr = [[0 for j in range(max_karo+10)] for i in range(max_sero+10)]


for re in result:

    for j in range (re[1],re[1]+10):
        for i in range (re[0],re[0]+10):
            arr[j][i] = 1

cnt = 0

for i in arr:
    cnt+=sum(i)
print(cnt)
