li = ["c=", "c-","dz=", "d-", "lj", "nj", "s=", "z="]
string = input()

cnt = 0

for check in li:
    cnt+=string.count(check)

print(len(string)-cnt)
