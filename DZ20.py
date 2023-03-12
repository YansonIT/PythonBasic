import random

def sort_matrix():
    M = int(input("Введіть розмір матриці: "))
    matrix = [[random.randint(1, 50) for j in range(M)] for i in range(M)]


    col_sums = [0] * M
    for i in range(M):
        for j in range(M):
            col_sums[j] += matrix[i][j]
            print(matrix[i][j], end="\t")
        print()

    # Виводимо суми стовпців
    for col_sum in col_sums:
        print(col_sum, end="\t")
    print()
    print("\n\n")

    # транспонування матриці
    for i in range(M):
        for j in range(i, M):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # сортування рядків матриці
    for i in range(M):
        if i % 2 == 0:
            for j in range(M - 1, 0, -1):
                for k in range(j):
                    if matrix[i][k] < matrix[i][k + 1]:
                        matrix[i][k], matrix[i][k + 1] = matrix[i][k + 1], matrix[i][k]
        else:
            for j in range(M - 1):
                for k in range(j, M):
                    if matrix[i][j] > matrix[i][k]:
                        matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]

    # повернення матриці в початковий стан
    for i in range(M):
        for j in range(i, M):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    #Виводимо відсортовавної матриці та суми стовпців
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

    for col_sum in col_sums:
        print(col_sum, end="\t")
    print()

sort_matrix()
