n = int(input())
A1 = [[int(i) for i in input().split()] for j in range(n)]
A2 = A1
x = int(input())
for _ in range(x-1):
    A = [[0] * n for j in range(n)]
    for i in range(n):
        for j in range(n):
            for kol_vo in range(n):
                A[i][j] += A1 [i][kol_vo] * A2[kol_vo][j]
    A1 = A
for i in A:
    print(*i)