import sys

P = int(input())

for _ in range(P):

    cnt = 0
    
    li = sys.stdin.readline().split()

    print(li[0], end=" ")

    li = list(map(int, li[1:]))

    for i in range(1, len(li)):
        value = li[i]
        j = i
        while j > 0 and li[j-1] > value:
            li[j] = li[j-1]
            j -= 1
            cnt += 1
        li[j] = value
    
    print(cnt)