x = input().split()
n, m = int(x[0]), int(x[1])
tt = [i for i in range(1, m + 1)]
A = []
for i in range(n):
    A.append(tt)
    tt = tt[1:] + [tt[0]]

for i in range(n):
    for j in range(m):
        print(str(A[i][j]).ljust(3), end='')
    print()