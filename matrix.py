class Matrix:
    def __init__(self, n, m, matrix=None):
        """
        Конструктор класса для инициализации разреженной матрицы
        :param n: Количество строк матрицы
        :param m: Количество столбцов матрицы
        :param matrix: Двумерный список, представляющий исходную матрицу
        """
        if not matrix:
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

    def __eq__(self, other):
        """
        Метод для проверки эквивалентности двух объектов класса Matrix.

        Два объекта считаются эквивалентными, если:
        1. Их размеры (количество строк и столбцов) совпадают.
        2. Их внутренние структуры разреженного представления (data, indices, ind_ptr) идентичны.

        :param other: Объект, с которым производится сравнение.
        :return: True, если объекты эквивалентны; False, если нет.
        """
        if not isinstance(other, Matrix):
            return False
        return (
                self.n == other.n and
                self.m == other.m and
                self.data == other.data and
                self.indices == other.indices and
                self.ind_ptr == other.ind_ptr
        )

    def get_element(self, i, j) -> float:
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

    def get_trace(self) -> float:
        """
        Метод для получения следа матрицы (сумма элементов на главной диагонали)
        :return: След матрицы, если она квадратная, иначе 0
        """
        if self.n == self.m:
            return sum([self.get_element(i, i) for i in range(self.n)])
        else:
            raise ValueError("Матрица должна быть квадратной")

    def to_dense(self):
        """
        Метод для преобразования CSR-матрицы в двумерный список
        :return: Двумерный список, представляющий плотную матрицу
        """
        dense_matrix = [[0] * self.m for _ in range(self.n)]

        if not self.data or all(value == 0 for value in self.data):
            return dense_matrix

        for i in range(self.n):
            for ind in range(self.ind_ptr[i], self.ind_ptr[i + 1]):
                j = self.indices[ind]
                dense_matrix[i][j] = self.data[ind]

        return dense_matrix
