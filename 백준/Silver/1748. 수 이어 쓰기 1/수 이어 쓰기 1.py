N = int(input())
result = 0 # 답

n = len(str(N)) # 글자수 길이


for i in range(n,0,-1):
    result += (N-(10**(i-1))+1)*(i)
    N = (10**(i-1))-1
print(result)