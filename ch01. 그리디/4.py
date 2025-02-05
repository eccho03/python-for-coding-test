import sys
n = int(input())
coin = list(map(int, sys.stdin.readline().split()))
coin.sort(reverse=True)

target = 1

while(True):
    result = target
    for i in coin:
        if i <= result:
            result -= i

    if result > 0:
        print(target)
        break
    target += 1