N = input()

zero_num = N.count('0')//2
one_num = N.count('1')//2

N = list(N)

total_num = len(N)

for i in range(len(N)):
    if N[i] == '1':
        N[i] = ''
        one_num-=1
    if one_num == 0:
        break
    
for i in range(len(N)-1,-1,-1):
    if N[i] == '0':
        N[i] = ''
        zero_num-=1
    if zero_num == 0:
        break
    
print(''.join(N))
