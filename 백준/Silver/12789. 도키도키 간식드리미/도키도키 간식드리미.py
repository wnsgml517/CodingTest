from collections import deque

def check(stack,i): # 스택에 넣을 건지 확인
    if len(stack)==0:
        return True
    elif i<stack[-1]:
        return True
    else:
        return False
def stackpop(stack, i): #스택에서 빼낼 건지 확인..
    if len(stack)==0:
        return False
    elif i == stack[-1]:
        return True
    else:
        return False
    
n = int(input())
li = list(map(int, input().split()))

stack = []

target = 1

queue = deque()

while len(li)>0:

    i = li[0]
    
    if i == target:
        li.remove(i)
        target+=1
    elif stackpop(stack, target):
        stack.remove(target)
        target+=1
    elif check(stack,i):
        li.remove(i)
        stack.append(i)
    else:
        break
    
if len(li)==0:
    print("Nice")
else:
    print("Sad")
