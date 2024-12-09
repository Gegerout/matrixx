import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):
    # Тест инициализации матрицы
    def test_init(self):
        matrix_data = [
            [3, 0, 2],
            [0, 1, 0],
            [0, 0, 5]
        ]
        matrix = Matrix(3, 3, matrix_data)

        # Проверяем, что после инициализации данные в разреженном формате соответствуют ожиданиям
        expected_data = [3, 2, 1, 5]
        expected_indices = [0, 2, 1, 2]
        expected_ind_ptr = [0, 2, 3, 4]

        self.assertEqual(matrix.data, expected_data)
        self.assertEqual(matrix.indices, expected_indices)
        self.assertEqual(matrix.ind_ptr, expected_ind_ptr)

    # Тест получения элемента матрицы
    def test_get_element(self):
        matrix_data = [
            [3, 0, 2],
            [0, 1, 0],
            [0, 0, 5]
        ]
        matrix = Matrix(3, 3, matrix_data)

        # Проверяем извлечение элементов
        self.assertEqual(matrix.get_element(0, 0), 3)
        self.assertEqual(matrix.get_element(0, 2), 2)
        self.assertEqual(matrix.get_element(1, 1), 1)
        self.assertEqual(matrix.get_element(2, 2), 5)

        # Проверяем элемент, которого нет в матрице (ноль)
        self.assertEqual(matrix.get_element(1, 2), 0)
        self.assertEqual(matrix.get_element(0, 1), 0)

    # Тест получения следа
    def test_get_trace(self):
        # Для квадратной матрицы
        matrix_data = [
            [3, 0, 2],
            [0, 1, 0],
            [0, 0, 5]
        ]
        matrix = Matrix(3, 3, matrix_data)
        self.assertEqual(matrix.get_trace(), 9)  # 3 + 1 + 5 = 9

        # Тест для неквадратной матрицы
        matrix_data_non_square = [
            [1, 2, 3],
            [4, 5, 6]
        ]
        matrix_non_square = Matrix(2, 3, matrix_data_non_square)
        self.assertEqual(matrix_non_square.get_trace(), 0)  # Неквадратная матрица не может иметь след


if __name__ == '__main__':
    unittest.main()
