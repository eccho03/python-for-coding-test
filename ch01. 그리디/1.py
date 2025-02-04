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
    