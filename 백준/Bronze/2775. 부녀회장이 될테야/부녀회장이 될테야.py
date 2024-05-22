N = int(input())

for _ in range (N):
    i = int(input())
    j = int(input())

    arr = [[0 for _ in range(j)] for _ in range(i+1)]


    for index in range(j):
        arr[0][index] = index+1
    
    
    
    for floor in range(1, i+1):
        for ho in range(j):
            for value in range(ho+1):                
                arr[floor][ho]+=arr[floor-1][value]
           
    print(arr[i][j-1], end =" ")
