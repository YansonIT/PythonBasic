import random

M = int(input("Введіть кількість рядків : "))
N = int(input("Введіть кількість стовпців : "))

matrix = [[random.randint(10, 50) for j in range(N)] for i in range(M)]

row_sums = [0] * M
col_sums = [0] * N

for i in range(M):
    for j in range(N):
        row_sums[i] += matrix[i][j]
        col_sums[j] += matrix[i][j]

        print("{:>5}".format(matrix[i][j]), end='')

    print("{:>7}".format(row_sums[i]))
    print()
for j in range(N):
    print("{:>5}".format(col_sums[j]), end='')

print()