class SparseMatrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = {}

    def set(self, row, col, value):
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols:
            raise ValueError("Invalid row or column index")
        if value == 0:
            raise ValueError("Invalid value: Dictionary cannot store value '0' ")
        else:
            self.matrix[(row, col)] = value

    def get(self, row, col):
        if row < 0 or col < 0 or row >= self.rows or col >= self.cols:
            raise ValueError("Invalid row or column index")
        return self.matrix.get((row, col), 0) 

    def recommend(self, vector):
        if len(vector) != self.cols:
            raise ValueError("Vector length does not match the number of columns")
        result = [0] * self.rows
        for (row, col), value in self.matrix.items():
            result[row] += value * vector[col]
        return result

    def add_movie(self, matrix):
        if matrix.rows != self.rows or matrix.cols != self.cols:
            raise ValueError("Matrix dimensions do not match")
        
        result_matrix = SparseMatrix(self.rows, self.cols)
        for (row, col), value in self.matrix.items():
            result_matrix.set(row, col, value)
        for (row, col), value in matrix.matrix.items():
            result_matrix.set(row, col, value)
        return result_matrix

    def to_dense(self):
        max_row = max(row for row, _ in self.matrix.keys())
        max_col = max(col for _, col in self.matrix.keys())
        dense_matrix = [[0] * (max_col + 1) for _ in range(max_row + 1)]
        for (row, col), value in self.matrix.items():
            dense_matrix[row][col] = value
        return dense_matrix


