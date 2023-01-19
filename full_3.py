n = int(input())
A = []
for i in range(n):
    tt = [0 for e in range(n)]
    A.append(tt)
for i in range(n):
    for j in range(n):
        if i <= j and i <= n - 1 - j:
            A[i][j] = 1
        elif i >= j and i >= n - 1 - j:
            A[i][j] = 1

for i in range(n):
    for j in range(n):
        print(str(A[i][j]).ljust(3), end='')
    print()