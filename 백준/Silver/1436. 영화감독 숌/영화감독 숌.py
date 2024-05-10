N = int(input())
result = 0 # 답
cnt = 0


while(1):
    result+=1
    if("666" in str(result)):
        cnt+=1

    if (cnt==N):
        print(result)
        break
