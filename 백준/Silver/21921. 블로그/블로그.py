import sys

N, X = map(int, input().split())
li = list(map(int, input().split()))

# 첫 번째 윈도우의 합을 계산합니다.
current_sum = sum(li[:X])
MAX = current_sum
cnt = 1

# 슬라이딩 윈도우를 이용하여 나머지 부분의 합을 계산합니다.
for i in range(N - X):
    # 현재 윈도우의 합에서 가장 왼쪽 값을 빼고, 오른쪽에 새로운 값을 더합니다.
    current_sum = current_sum - li[i] + li[i + X]
    
    if MAX < current_sum:
        MAX = current_sum
        cnt = 1
    elif MAX == current_sum:
        cnt += 1

# 모든 숫자의 합이 0인 경우를 처리합니다.
if MAX == 0:
    print("SAD")
    sys.exit()

print(MAX)
print(cnt)