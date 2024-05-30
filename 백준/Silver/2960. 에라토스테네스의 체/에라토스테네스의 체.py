import sys

N, K = list(map(int,input().split()))

cnt = 0
stack = []
P = 2

for i in range (2,N+1):
    stack.append(i)

while True:

    n = 1
    
    while (P*n <= stack[-1]):
        if P*n in stack:
            stack.remove(P*n)
            cnt+=1
        if cnt == K:
            print(P*n)
            sys.exit()
        n+=1
        
    P = stack[0]
