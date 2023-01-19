num1 = int(input())
A = []
for i in range(num1):
    tt = [int(j) for j in range(num1)]
    A.append(tt)

for i in range(num1):
    for j in range(num1):
        if i == num1 - 1 - j:
            A[i][j] = 1
        elif i < num1 - 1 - j:
            A[i][j] = 0
        elif i > num1 - 1 - j:
            A[i][j] = 2
for i in range(num1):
    print(*A[i])