x = input().split()
n, m = int(x[0]), int(x[1])
mat = []
for i in range(n):
    tt = [i for i in range(m)]
    mat.append(tt)

for i in range(n):
    for j in range(m):
        if (i + j) % 2 == 0:
            mat[i][j] = "."
        else:
            mat[i][j] = "*"

for i in range(n):
    print(*mat[i])