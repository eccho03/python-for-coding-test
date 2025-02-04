s = input()
arr = list(s)
intarr = list(map(int, arr))

result = 0

if intarr[0] * intarr[1] > intarr[0] + intarr[1]:
            result += intarr[0] * intarr[1]
else:
    result += intarr[0] + intarr[1]

for i in range(2, len(s)):
    if result * intarr[i] > result + intarr[i]:
        result *= intarr[i]
    else:
        result += intarr[i]

print(result)