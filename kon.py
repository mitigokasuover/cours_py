num1 = 8
x, y = input()

A = [["."] * num1 for __ in range(num1)]

y = num1 - int(y)
x = ord(x) - 97
A[y][x] = "N"

for i in range(num1):
    for j in range(num1):
        if abs(i - y) * abs(j - x) == 2:
            A[i][j] = "*"
for i in range(num1):
    print(*A[i])
