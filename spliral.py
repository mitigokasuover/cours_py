spik = input().split()
n, m = int(spik[0]), int(spik[1])
A = []
for i in range(n):
    tt = [0 for r in range(m)]
    A.append(tt)

x, y = 0, 0
sh1, sh2 = 0, 1
A[0][0] = 1
cc = 2
while cc <= n * m:
    if 0 <= x + sh1 <= n - 1 and 0 <= y + sh2 <= m - 1 and A[x + sh1][y + sh2] == 0:
        A[x + sh1][y + sh2] = cc
        cc += 1
        x += sh1
        y += sh2
    else:
        if sh2 == 1:
            sh2 = 0
            sh1 = 1
        elif sh1 == 1:
            sh1 = 0
            sh2 = -1
        elif sh2 == -1:
            sh2 = 0
            sh1 = -1
        elif sh1 == -1:
            sh1 = 0
            sh2 =  1

for i in range(n):
    for j in range(m):
        print(str(A[i][j]).ljust(3), end="")
    print()      