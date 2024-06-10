from collections import deque
import sys

def isEmptyQueueFront(queue):
    if len(queue) == 0:
        print(-1)
        return False
    else:
        print(queue[0])
        return True

def isEmptyQueueBack(queue):
    if len(queue) == 0:
        print(-1)
        return False
    else:
        print(queue[-1])
        return True    

N = int(input())
queue = deque()
mode = ["push_front", "push_back", "pop_front","pop_back","size","empty","front","back"]

for i in range(N):
    st = sys.stdin.readline().split(" ")
    m = mode.index(st[0].strip())

    if m == 0:
        queue.appendleft(st[1].strip())
    elif m == 1:
        queue.append(st[1].strip())
    elif m == 2:
        if isEmptyQueueFront(queue):
            queue.popleft()
    elif m == 3:
        if isEmptyQueueBack(queue):
            queue.pop()
    elif m == 4:
        print(len(queue))
    elif m == 5:
        if len(queue):
            print(0)
        else:
            print(1)
    elif m == 6:
        isEmptyQueueFront(queue)
    elif m == 7:
        isEmptyQueueBack(queue)
