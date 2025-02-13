s = str(input())

string = list(map(str, str(s)))

for i in string:
    if i == 0 or i == 1:
        i = int(i)
print(string)