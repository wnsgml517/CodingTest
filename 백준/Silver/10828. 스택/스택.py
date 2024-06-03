import sys

N = int(sys.stdin.readline())

stack = []
mode = {"pop": 0 ,"size":1,"empty":2,"top":3,"push":4}

for i in range (N):
    li = sys.stdin.readline().split()
    
    
    index = mode[li[0]]

    if index == 4:
        stack.append(li[1])
        continue
    
    n = len(stack)
    
    if index == 0:
        if n==0:
            print(-1)
        else:
            print(stack.pop())
            
    elif index == 1:
        print(len(stack))

    elif index == 2:
        if n==0:
            print(1)
        else:
            print(0)

    elif index == 3:
        if n == 0:
            print(-1)
        else:
            print(stack[-1])

    

