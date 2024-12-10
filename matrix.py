import typing as tp


class Matrix:
    def __init__(self, n, m, matrix=None):
        """
        Конструктор класса для инициализации разреженной матрицы
        :param n: Количество строк матрицы
        :param m: Количество столбцов матрицы
        :param matrix: Двумерный список, представляющий исходную матрицу
        """
        if matrix is None:
            matrix = [[0 for __ in range(m)] for _ in range(n)]
        self.n = n
        self.m = m
        self.data = []  # данные в разреженном формате
        self.indices = []  # индексы столбцов элементов data
        self.ind_ptr = []  # индексы начала каждой строки в массиве data

        # преобразование матрицы в разреженную
        for i in range(n):
            self.ind_ptr.append(len(self.data))
            for j in range(m):
                if matrix[i][j] != 0:
                    self.data.append(matrix[i][j])
                    self.indices.append(j)

        self.ind_ptr.append(len(self.data))

    def get_element(self, i, j):
        """
        Метод для получения элемента разреженной матрицы по индексу (i, j)
        :param i: Индекс строки
        :param j: Индекс столбца
        :return: Элемент матрицы по индексу (i, j), если он существует, иначе 0
        """
        for ind in range(len(self.data)):
            if self.indices[ind] == j and self.ind_ptr[i] <= ind < self.ind_ptr[i + 1]:
                return self.data[ind]
        else:
            return 0

    def get_trace(self):
        """
        Метод для получения следа матрицы (сумма элементов на главной диагонали)
        :return: След матрицы, если она квадратная, иначе 0
        """
        if self.n == self.m:
            return sum([self.get_element(i, i) for i in range(self.n)])
        else:
            return 0
