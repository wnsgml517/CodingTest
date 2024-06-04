import sys

N = int(sys.stdin.readline())

cnt = 0
edge = 1
i = 1

while (True): # 1부터 N까지 변화...
    cnt+=i
    if cnt>=N:
        break
    
    i+=1

start = i+N-cnt
end = i- start+1

if i %2 == 0:
    print(f"{start}/{end}")
else:
    print(f"{end}/{start}")
