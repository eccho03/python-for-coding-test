import sys

n = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

group = 0
cur = 0

for i in arr:
    cur += 1
    if cur >= i:
        group += 1
        cur = 0

print(group)

# sort 하는 접근까지 좋았는데 그 이후의 생각이 아쉬웠다.
# 생각이 잘 나지 않을 땐 입출력 예시를 보고 어떻게 나온건지 다시 한 번 생각해보고,
# 어떤 경우에 그것대로 가는지 다시 한 번 생각해보기
