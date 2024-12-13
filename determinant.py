from matrix import Matrix


def get_dense_submatrix(matrix: Matrix, excluded_row: int, excluded_col: int):
    """
    Возвращает матрицу с удалением указанных столбца и строки
    :param matrix: исходная матрица
    :param excluded_row: строка, которую нужно исключить
    :param excluded_col: столбец, который нужно исключить
    :return: Подматрица без указанной строки и столбца
    """
    dense_matrix = []
    for i in range(matrix.n):
        if i == excluded_row:
            continue
        row = []
        for j in range(matrix.m):
            if j == excluded_col:
                continue
            row.append(matrix.get_element(i, j))
        dense_matrix.append(row)
    return dense_matrix


def count_determinant(matrix: Matrix) -> float:
    """
    Функция для подсчета определителя матрицы
    :param matrix: исходная матрица
    :return: Определитель матрицы
    """
    # Простой случай матрица 1 на 1
    if matrix.n == 1 and matrix.m == 1:
        return matrix.get_element(0, 0)

    # Простой случай матрица 2 на 2
    if matrix.n == 2 and matrix.m == 2:
        a = matrix.get_element(0, 0)
        b = matrix.get_element(0, 1)
        c = matrix.get_element(1, 0)
        d = matrix.get_element(1, 1)
        return a * d - b * c

    determinant = 0
    for col in range(matrix.m):
        submatrix_data = get_dense_submatrix(matrix, excluded_row=0, excluded_col=col)
        submatrix = Matrix(len(submatrix_data), len(submatrix_data[0]), submatrix_data)

        cofactor = ((-1) ** col) * matrix.get_element(0, col) * count_determinant(submatrix)
        determinant += cofactor

    return determinant


def solve(matrix: Matrix):
    determinant = count_determinant(matrix)

    return determinant, determinant != 0
