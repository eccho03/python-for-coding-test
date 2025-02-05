import sys

s = sys.stdin.readline().rstrip()
cnt_0 = 0
cnt_1 = 0
result = 0
reverse_s = ""
for i in range(len(s)):
    a = (int(s[i]))
    if a == 0:
        a = 1
        cnt_1 += 1
    else:
        a = 0
        cnt_0 += 1
    
    reverse_s += str(a)

for i in range(len(reverse_s)-1):
    a = int(reverse_s[i])
    b = int(reverse_s[i+1])

    if a != b:
        if cnt_0 > cnt_1:
            if a == 1:
                result += 1
            else:
                continue
        else:
            if a == 0:
                result += 1 

print(result)