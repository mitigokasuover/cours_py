x = input().split()
n, m = int(x[0]), int(x[1])
A = []
for i in range(n):
    tt = [j for j in range(m)]
    A.append(tt)

cc = 1
for i in range(n * m):
    for j in range(n):
        for ij in range(m):
            if j + ij == i:
                A[j][ij] = cc
                cc += 1

for i in range(n):
    for j in range(m):
        print(str(A[i][j]).ljust(3), end = "")
    print()