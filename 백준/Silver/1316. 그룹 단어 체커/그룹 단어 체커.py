N = int(input())
cnt = 0

def wordChecker(string):
    for s in string:
        if s not in check:
            check.append(s)
        elif check[-1] != s:
            return False

    return True

for i in range(N):

    check = []
    
    string = input()

    if wordChecker(string):
        cnt+=1
        
print(cnt)    
