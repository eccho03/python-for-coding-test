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

    # 동전의 개수가 한정적인 경우
    # 빼는 방법 말고 더해서 구하는 방법이 있다는 것도 생각하기
    # 알고리즘을 최대한 간결하게 짜도록 연습하기
