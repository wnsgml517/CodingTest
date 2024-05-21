n = int(input())

li = []

for i in range(n):
    n = int(input())

    if n!= 0:
        li.append(n)

    else:
        li.pop()

print(sum(li))
