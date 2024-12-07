class Matrix:
    def __init__(self, n, m, matrix): # n - количество строк, m - количество столбцов
        self.n = n
        self.m = m
        self.data = [] # данные в разреженном формате
        self.indices = [] # индексы столбцов элементов data
        self.ind_ptr = [] # индексы начала каждой строки в массиве data

        # преобразование матрицы в разреженную
        data_ind = 0  # удобно сохранияем инждекс последнего ненулевого элемента в data
        for i in range(n):
            flag = False
            for j in range(m):
                if matrix[i][j] != 0:
                    self.data.append(matrix[i][j])
                    self.indices.append(j)
                    if not flag:
                        self.ind_ptr.append(data_ind)
                    data_ind += 1
                    flag = True

        self.ind_ptr.append(len(self.data))

    # получение элемента разреженной матрицы по заданным индексам
    def get_element(self, i, j):
        for ind in range(len(self.data)):
            if self.indices[ind] == j and self.ind_ptr[i] <= ind < self.ind_ptr[i + 1]:
                return self.data[ind]
        else:
            return 0

    # получение следа (с использованием get_element)
    def get_trace(self):
        if self.n == self.m:
            return sum([self.get_element(i, i) for i in range(self.n)])
        else:
            return 0
