from determinant import solve
from matrix import Matrix
from operations import sum_matrix, scalar_matrix, multiplication_matrix

print("Введите размеры первой матрицы")
n, m = map(int, input().split())
print("Введите строки первой матрицы")
data = []

for i in range(n):
    data.append(list(map(int, input().split())))

matrix = Matrix(n, m, data)
i = 0
j = 0

print("Элемент матрицы в строке {} и столбце {}:".format(i, j), matrix.get_element(0, 0))
print("След матрицы:", matrix.get_trace())

print("Введите размеры второй матрицы")
n, m = map(int, input().split())
print("Введите строки второй матрицы")
data2 = []

for i in range(n):
    data2.append(list(map(int, input().split())))

matrix2 = Matrix(n, m, data2)

scalar = 4

matrix_sum = sum_matrix(matrix, matrix2)
matrix_scalar = scalar_matrix(matrix, scalar)
matrix_mul = multiplication_matrix(matrix, matrix2)

print("Сложение матрицы")
for row in matrix_sum.to_dense():
    print(*row)
print("Умножение матрицы на скаляр {}".format(scalar))
for row in matrix_scalar.to_dense():
    print(*row)
print("Умножение матриц")
for row in matrix_mul.to_dense():
    print(*row)

det_matrix, has_reverse = solve(matrix)

print("Определитель первой матрицы:", det_matrix)
print("Имеет ли обратную матрицу:", "Да" if det_matrix else "Нет")
