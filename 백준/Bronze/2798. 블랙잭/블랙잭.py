from itertools import combinations

N,M = list(map(int,input().split()))
arr = list(map(int,input().split()))

arr.sort()

min = 300000

for i in combinations(arr,3):
    n = M - sum(list(i))
    
    if (n>=0 and n <= min):
        min = n
        
print(M-min)
