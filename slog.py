x = input().split()
n,m = int(x[0]), int(x[1])
A1 = [[int(x) for x in input().split()] for _ in range(n)]
tt = input()
A2 = [[int(x) for x in input().split()] for _ in range(n)]
A3 = [[int(x) for x in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        A3[i][j] = A1[i][j] + A2[i][j]

for i in range(n):
    print(*A3[i])