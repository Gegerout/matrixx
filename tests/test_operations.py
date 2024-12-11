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
        self.assertEqual(summ, Matrix(2, 3, [[1, 4, 2], [5, 3, 6]]))

    # Тестирование умножения на скаляр
    def test_scalar(self):
        scalar = scalar_matrix(2, self.A)
        self.assertEqual(scalar.get_element(0, 0), 2)
        self.assertEqual(scalar.get_element(0, 1), 0)
        self.assertEqual(scalar.get_element(0, 2), 4)
        self.assertEqual(scalar.get_element(1, 0), 0)
        self.assertEqual(scalar.get_element(1, 1), 6)
        self.assertEqual(scalar.get_element(1, 2), 0)

    # Тестирование умножения матриц
    def test_multiplication(self):
        multiplication = multiplication_matrix(self.A, self.E)
        self.assertEqual(multiplication.get_element(0, 0), 7)
        self.assertEqual(multiplication.get_element(0, 1), 10)
        self.assertEqual(multiplication.get_element(1, 0), 0)
        self.assertEqual(multiplication.get_element(1, 1), 0)

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
