N, K = list(map(int,input().split()))

li =  list(input())

check = [0] * (len(li))

# 못 먹는 사람 수 세기...
for i, value in enumerate(li):
    if value == 'P':
        start = 0 if (i - K)<= 0 else i - K
        end = N-1 if (i + K)>= N else i + K
        
        for search in range (start,end+1):
            if check[search] == 0 and li[search] == 'H':
                check[search] = 1
                break


print(check.count(1))
