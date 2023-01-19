num1 = int(input())

A = [list(map(int, input().split())) for __ in range(num1)]

for i in range(num1):
    for j in range(num1 - 1, -1, -1):
        print(A[j][i], end=' ')
    print()