num1 = int(input())

A = [list(map(int, input().split())) for __ in range(num1)]

kol_vo = [i for i in range(1, num1**2 + 1)]

t1, t2 = 0, 0
for i in range(num1):
    sum_st, sum_rad = 0, 0
    for j in range(num1):
        sum_st += A[j][i]
        sum_rad += A[i][j]
        if A[i][j] in kol_vo:
            kol_vo.remove(A[i][j])
    t1 += A[i][i]
    t2 += A[i][num1 - i - 1]
    if sum_st != sum_rad:
        break

if sum_rad == sum_st == t1 == t2 and kol_vo == []:
    print("YES")
else:
    print("NO")