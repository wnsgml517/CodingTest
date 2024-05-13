def check(i):
    if (len(str(i))<=2):
        return True
    
    diff = int(str(i)[1]) - int(str(i)[0])
    
    for index in range (1,len(str(i))):
        if (diff != int(str(i)[index]) - int(str(i)[index-1])):
            return False
    return True
        
N = int(input())
cnt = 0

for i in range(1,N+1):
    if check(i):
       cnt+=1

print(cnt)
