num1 = int(input())
num2 = int(input())
A = [[0] * num2 for i in range(num1)]

for i in range(num1):
    for j in range(num2):
        A[i][j] = i * j

for i in range(num1):
    for i in range(num2):
        print(str(A[i][j]).ljust(3))
