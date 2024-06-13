import sys

input = sys.stdin.read
data = input().split()

P = int(data[0])
index = 1

for _ in range(P):
    cnt = 0
    li = list(map(int, data[index+1:index+21]))
    index += 21
    
    sorted_list = []
    for i, value in enumerate(li):
        pos = i
        while pos > 0 and sorted_list[pos-1] > value:
            pos -= 1
        sorted_list.insert(pos, value)
        cnt += i - pos

    print(data[index-21], cnt)