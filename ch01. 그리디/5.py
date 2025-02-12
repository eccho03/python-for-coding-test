import sys

n, m = map(int, sys.stdin.readline().split())
ball = list(map(int, sys.stdin.readline().split()))

cnt = 0
for i in ball:
    for j in ball:
        if i != j:
            cnt += 1
print(cnt//2)