x,y,w,h = list(map(int,input().split()))

y_value = y if h - y > y else h - y
x_value = x if w - x > x else w - x

result = x_value if y_value > x_value else y_value

print(result)
