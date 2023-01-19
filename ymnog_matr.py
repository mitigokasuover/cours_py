n, m = [int(i) for i in input().split]
A1 = [[int(i) for i in input().split()] for j in range(n)]
input()
n1, m1 = [int(i) for i in input().split]
A2 = [[int(i) for i in input().split] for j in range(n1)]
A = [[0] * m1 for i in range(n)]

for i in range(n):
    for j in range(m1):
        for kol_vo in range(m):
            A[i][j] += A1 [i][kol_vo] * A2[kol_vo][j]

for i in A:
    print(*i)