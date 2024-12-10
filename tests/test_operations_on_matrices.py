import unittest
from matrix import Matrix
from operations_on_matrices import sum_matrix, scalar_matrix, multiplication_matrix


class TestMatrixOperations(unittest.TestCase):

    def setUp(self):
        """Создаем тестовые матрицы перед каждым тестом."""
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

    def test_sum_matrix(self):
        """Тестирование сложения матриц."""
        C = sum_matrix(self.A, self.B)
        self.assertEqual(C.get_element(0, 0), 1)
        self.assertEqual(C.get_element(0, 1), 4)
        self.assertEqual(C.get_element(0, 2), 2)
        self.assertEqual(C.get_element(1, 0), 5)
        self.assertEqual(C.get_element(1, 1), 3)
        self.assertEqual(C.get_element(1, 2), 6)

    def test_scalar_matrix(self):
        """Тестирование скалярного умножения."""
        D = scalar_matrix(2, self.A)
        self.assertEqual(D.get_element(0, 0), 2)
        self.assertEqual(D.get_element(0, 1), 0)
        self.assertEqual(D.get_element(0, 2), 4)
        self.assertEqual(D.get_element(1, 0), 0)
        self.assertEqual(D.get_element(1, 1), 6)
        self.assertEqual(D.get_element(1, 2), 0)

    def test_multiplication_matrix(self):
        """Тестирование умножения матриц."""
        F = multiplication_matrix(self.A, self.E)
        self.assertEqual(F.get_element(0, 0), 7)
        self.assertEqual(F.get_element(0, 1), 10)
        self.assertEqual(F.get_element(1, 0), 0)
        self.assertEqual(F.get_element(1, 1), 0)

    def test_invalid_sum_matrix(self):
        """Тестирование выброса исключения при неправильных размерах матриц."""
        G = Matrix(3, 3, [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ])
        with self.assertRaises(ValueError):
            sum_matrix(self.A, G)

    def test_invalid_multiplication_matrix(self):
        """Тестирование выброса исключения при неправильных размерах матриц."""
        G = Matrix(2, 3, [
            [1, 2, 1],
            [3, 4, 5]
        ])
        with self.assertRaises(ValueError):
            multiplication_matrix(self.A, G)



if __name__ == "__main__":
    unittest.main()
