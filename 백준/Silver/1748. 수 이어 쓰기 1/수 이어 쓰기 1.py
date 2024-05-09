N = int(input())
check = N
n = 0
result = 0

while(check): # 자릿수 세기
    n+=1
    check=check//10


for i in range(n,0,-1):
    result += (N-(10**(i-1))+1)*(i)
    N = (10**(i-1))-1
print(result)
