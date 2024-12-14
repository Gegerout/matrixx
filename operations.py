from matrix import Matrix


def sum_matrix(mat1: Matrix, mat2: Matrix) -> Matrix:
    """
    Функция для сложения двух разреженных матриц.

    :param mat1: Первая разреженная матрица.
    :param mat2: Вторая разреженная матрица.
    :return: Новая разреженная матрица, результат сложения.
    :raises ValueError: Если размерности матриц не совпадают.
    """
    # Проверка, совпадают ли размеры матриц
    if mat1.n != mat2.n or mat1.m != mat2.m:
        raise ValueError("Размерности матриц должны совпадать для сложения")

    result_data = []
    result_indices = []
    result_ind_ptr = [0]
    curr_ptr = 0

    # Обход по строкам матриц
    for i in range(mat1.n):
        for j in range(mat1.m):
            if not (mat1.get_element(i, j) == 0 and mat2.get_element(i, j) == 0):
                result_data.append(mat1.get_element(i, j) + mat2.get_element(i, j))
                result_indices.append(j)
                curr_ptr += 1
            if j == mat1.m - 1:
                result_ind_ptr.append(curr_ptr)

    new_matrix = Matrix(mat1.n, mat1.m)
    new_matrix.data = result_data
    new_matrix.indices = result_indices
    new_matrix.ind_ptr = result_ind_ptr

    return new_matrix


def scalar_matrix(mat1: Matrix, scal: int) -> Matrix:
    """
    Функция для скалярного умножения разреженной матрицы.
    :param scal: Скаляр для умножения.
    :param mat1: Разреженная матрица.
    :return: Новая разреженная матрица, результат скалярного умножения.
    """
    result_data = [value * scal for value in mat1.data]

    new_matrix = Matrix(mat1.n, mat1.m)
    new_matrix.data = result_data
    new_matrix.indices = mat1.indices.copy()
    new_matrix.ind_ptr = mat1.ind_ptr.copy()

    return new_matrix


def multiplication_matrix(mat1: Matrix, mat2: Matrix) -> Matrix:
    """
    Функция для умножения двух разреженных матриц.

    :param mat1: Первая разреженная матрица.
    :param mat2: Вторая разреженная матрица.
    :return: Новая разреженная матрица, результат умножения.
    :raises ValueError: Если количество столбцов первой матрицы не совпадает с количеством строк второй.
    """
    if mat1.m != mat2.n:
        raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй")

    result_data = []
    result_indices = []
    result_ind_ptr = [0]
    curr_ptr = 0

    for i in range(mat1.n):
        if mat1.ind_ptr[i + 1] - mat1.ind_ptr[i] == 0:
            result_ind_ptr.append(result_ind_ptr[-1])
            continue
        cnt = 0
        for j in range(mat2.m):
            if j not in mat2.indices:
                cnt += 1
                continue
            curr_value = 0
            for k in range(mat1.m):
                curr_value += mat1.get_element(i, k) * mat2.get_element(k, j)
                if k == mat1.m - 1:
                    if curr_value != 0:
                        curr_ptr += 1
                        result_data.append(curr_value)
                        result_indices.append(j)
                        if j == mat2.m - 1:
                            result_ind_ptr.append(curr_ptr)
        if cnt == mat2.m:
            result_ind_ptr.append(result_ind_ptr[-1])

    if result_ind_ptr.count(0) != mat1.n + 1:
        result_ind_ptr.append(result_ind_ptr[-1])
    new_matrix = Matrix(mat1.n, mat2.m)
    new_matrix.data = result_data
    new_matrix.indices = result_indices
    new_matrix.ind_ptr = result_ind_ptr

    return new_matrix
