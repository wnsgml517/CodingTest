import math

l = int(input())
cnt = int(input())
spot = list(map(int, input().split()))

gap = max(spot[0],l-spot[-1])

for i in range (0,cnt-1):
    gap = max(gap,math.ceil((spot[i+1]-spot[i])/2))

print(gap)
