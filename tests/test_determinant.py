import unittest
from matrix import Matrix
from determinant import count_determinant


class TestDeterminant(unittest.TestCase):
    # Тест для матрицы 1x1
    def test_1x1(self):
        matrix_data = [[5]]
        matrix = Matrix(1, 1, matrix_data)
        self.assertEqual(count_determinant(matrix), 5)

    # Тест для матрицы 2x2
    def test_2x2(self):
        matrix_data = [
            [3, 4],
            [2, 1]
        ]
        matrix = Matrix(2, 2, matrix_data)
        self.assertEqual(count_determinant(matrix), -5)

    # Тест для матрицы 3x3
    def test_3x3(self):
        matrix_data = [
            [1, 2, 3],
            [0, 4, 5],
            [0, 0, 6]
        ]
        matrix = Matrix(3, 3, matrix_data)
        self.assertEqual(count_determinant(matrix), 24)

    def test_4x4(self):
        # Тест для матрицы 4x4
        matrix_data = [
            [1, 0, 0, 0],
            [2, 3, 0, 0],
            [4, 5, 6, 0],
            [7, 8, 9, 10]
        ]
        matrix = Matrix(4, 4, matrix_data)
        self.assertEqual(count_determinant(matrix), 180)

    # Тест для вырожденной матрицы (определитель должен быть равен 0)
    def test_singular_matrix(self):
        matrix_data = [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ]
        matrix = Matrix(3, 3, matrix_data)
        self.assertEqual(count_determinant(matrix), 0)

    # Тест для большой матрицы
    def test_large_matrix(self):
        matrix_data = [
            [1, 2, 3, 4, 7],
            [5, 1, 2, 3, 4],
            [8, 11, 1, 2, 76],
            [7, 22, 8, 1, 34],
            [9, 19, 2, 5, 91],
        ]
        matrix = Matrix(5, 5, matrix_data)
        self.assertEqual(count_determinant(matrix), 76671)


if __name__ == '__main__':
    unittest.main()
