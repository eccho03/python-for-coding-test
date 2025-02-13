s = input()

string = list(s)

number = "1234567890"

arr_num = []
arr_str = []

for i in range(len(string)):
    if number.find(string[i]) != -1:
        string[i] = int(string[i])
        arr_num.append(string[i])
    else:
        arr_str.append(string[i])

arr_str.sort()

for i in arr_str:
    print(i, end='')

sum_int = 0

for i in arr_num:
    sum_int += i
print(sum_int)