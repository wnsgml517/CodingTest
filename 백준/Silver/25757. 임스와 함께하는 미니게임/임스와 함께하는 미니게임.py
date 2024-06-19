import sys

dic = {'Y':2, 'F':3,'O':4}

num, mode = input().split()

mode = dic[mode]
total = []

for i in range (int(num)):
    total.append(sys.stdin.readline())
        
total = set(total)
print(len(total)//(mode-1))
