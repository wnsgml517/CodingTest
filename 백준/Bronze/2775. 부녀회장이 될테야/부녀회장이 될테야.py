N = int(input())

maxi = 0
maxj = 0

li = []

for _ in range (N):
    i = int(input())
    j = int(input())

    li.append((i,j))
    
    maxi = max(i,maxi)
    maxj = max(j, maxj)
    
for _ in range (N):

    arr = [[0 for _ in range(maxj)] for _ in range(maxi+1)]


    for index in range(maxj):
        arr[0][index] = index+1
    
    
    
    for floor in range(1, maxi+1):
        for ho in range(maxj):
            arr[floor][ho] = arr[floor-1][ho]+arr[floor][ho-1]


for i in li:
    print(arr[i[0]][i[1]-1], end =" ")
