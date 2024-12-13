import unittest
from matrix import Matrix
from operations import sum_matrix, scalar_matrix, multiplication_matrix


class TestMatrixOperations(unittest.TestCase):

    # Инициализация тестовых данных
    def setUp(self):
        self.A = Matrix(2, 3, [
            [1, 0, 2],
            [0, 3, 0]
        ])

        self.B = Matrix(2, 3, [
            [0, 4, 0],
            [5, 0, 6]
        ])

        self.E = Matrix(3, 2, [
            [1, 2],
            [0, 0],
            [3, 4]
        ])

    # Тестирование сложения матриц
    def test_sum(self):
        summ = sum_matrix(self.A, self.B)
        answer = Matrix(2, 3, [[1, 4, 2], [5, 3, 6]])
        self.assertEqual(summ, answer)

    # Тестирование умножения на скаляр
    def test_scalar(self):
        scalar = scalar_matrix(self.A, 2)
        answer = Matrix(2, 3, [
            [2, 0, 4],
            [0, 6, 0]
        ])
        self.assertEqual(scalar, answer)

    # Тестирование умножения матриц
    def test_multiplication(self):
        multiplication = multiplication_matrix(self.A, self.E)
        answer = Matrix(2, 2, [
            [7, 10],
            [0, 0]
        ])
        self.assertEqual(multiplication, answer)

    # Ожидание ошибки при неправильных размерах матриц
    def test_invalid_sum(self):
        init_matrix = Matrix(3, 3, [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        with self.assertRaises(ValueError):
            sum_matrix(self.A, init_matrix)

    # Ожидание ошибки при неправильных размерах матриц
    def test_invalid_multiplication(self):
        init_matrix = Matrix(2, 3, [
            [1, 2, 1],
            [3, 4, 5]
        ])
        with self.assertRaises(ValueError):
            multiplication_matrix(self.A, init_matrix)


if __name__ == "__main__":
    unittest.main()
