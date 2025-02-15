import sys

n = int(sys.stdin.readline().rstrip())
num = list(map(int, str(n)))

t = len(num)

left= 0
right = 0

for i in range(t//2):
    left += num[i]

for i in range(t//2, t):
    right += num[i]

if left == right:
    print("LUCKY")
else:
    print("READY")

# left와 right 변수 2개가 아닌
# 하나의 변수로 더한 값 - 뺀 값이 0인지 확인하는 방식을 쓰면 더 간결해진다.