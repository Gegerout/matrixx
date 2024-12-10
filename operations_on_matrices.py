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


def scalar_matrix(scal: int, mat1: Matrix) -> Matrix:
    """
    Функция для скалярного умножения разреженной матрицы.
    :param scal: Скаляр для умножения.
    :param mat1: Разреженная матрица.
    :return: Новая разреженная матрица, результат скалярного умножения.
    """
    result_data = [value * scal for value in mat1.data]
    # Возвращаем новую матрицу с изменёнными значениями, а не изменяем исходную
    new_matrix = Matrix(mat1.n, mat1.m)
    new_matrix.data = result_data
    new_matrix.indices = mat1.indices.copy()
    new_matrix.ind_ptr = mat1.ind_ptr.copy()
    return new_matrix

    return mat1


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
    for i in range(mat1.n + 1):
        if mat1.ind_ptr[i] - mat1.ind_ptr[i - 1] == 0:
            result_ind_ptr.append(curr_ptr)
            continue
        for j in range(mat2.m):
            if j not in mat2.indices:
                continue
            curr_value = 0
            for k in range(mat1.m):
                curr_value += mat1.get_element(i - 1, k) * mat2.get_element(k, j)
                if k == mat1.m - 1:
                    if curr_value != 0:
                        curr_ptr += 1
                        result_data.append(curr_value)
                        result_indices.append(j)
                        if j == mat2.m - 1:
                            result_ind_ptr.append(curr_ptr)
    result_ind_ptr.append(result_ind_ptr[-1])
    new_matrix = Matrix(mat1.n, mat2.m)
    new_matrix.data = result_data
    new_matrix.indices = result_indices
    new_matrix.ind_ptr = result_ind_ptr
    return new_matrix


# Тесты для функций
def test_matrix_operations():
    # Создаем тестовые матрицы
    A = Matrix(2, 3, [
        [1, 0, 2],
        [0, 3, 0]
    ])

    B = Matrix(2, 3, [
        [0, 4, 0],
        [5, 0, 6]
    ])

    # Тестирование сложения матриц
    C = sum_matrix(A, B)
    assert C.get_element(0, 0) == 1
    assert C.get_element(0, 1) == 4
    assert C.get_element(0, 2) == 2
    assert C.get_element(1, 0) == 5
    assert C.get_element(1, 1) == 3
    assert C.get_element(1, 2) == 6

    # Тестирование скалярного умножения
    D = scalar_matrix(2, A)
    assert D.get_element(0, 0) == 2
    assert D.get_element(0, 1) == 0
    assert D.get_element(0, 2) == 4
    assert D.get_element(1, 0) == 0
    assert D.get_element(1, 1) == 6
    assert D.get_element(1, 2) == 0

    # Создаем еще одну матрицу для умножения
    E = Matrix(3, 2, [
        [1, 2],
        [0, 0],
        [3, 4]
    ])

    # Тестирование умножения матриц
    F = multiplication_matrix(A, E)
    assert F.get_element(0, 0) == 7
    assert F.get_element(0, 1) == 10
    assert F.get_element(1, 0) == 0
    assert F.get_element(1, 1) == 0

    print("Все тесты пройдены успешно!")


# Запуск тестов
if __name__ == "__main__":
    test_matrix_operations()
