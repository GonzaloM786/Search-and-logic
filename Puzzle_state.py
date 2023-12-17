import numpy as np

class puzzle_state:

    def __init__(self, matrix, g):
        self.matrix = matrix
        self.g = g
        self.f = self.calculate_f(g)

    @staticmethod
    def coordinates(n):
        list = [[2,2], [0,0], [0,1],
                [0,2], [1,0], [1,1],
                [1,2],[2,0], [2,1]]
        return list[n]

    def calculate_f(self, G):
        h = 0
        for x in range(3):
            for y in range(3):
                num = self.matrix[x, y]
                if num != 0:
                    i, j = puzzle_state.coordinates(num)
                    h += abs(x-i) + abs(y-j)
        return G + h

    def neighbors(self):
        l_neighbors = []
        for x in range(3):
            for y in range(3):
                if self.matrix[x, y] == 0:
                    i, j = x, y
                    break
            else:
                continue
            break
        if i+1 < 3:
            new_matrix = self.matrix.copy()
            new_matrix[i, j] = new_matrix[i+1, j]
            new_matrix[i+1, j] = 0
            l_neighbors += [puzzle_state(new_matrix, self.g + 1)]
        if i-1 >= 0:
            new_matrix = self.matrix.copy()
            new_matrix[i, j] = new_matrix[i-1, j]
            new_matrix[i-1, j] = 0
            l_neighbors += [puzzle_state(new_matrix, self.g + 1)]
        if j+1 < 3:
            new_matrix = self.matrix.copy()
            new_matrix[i, j] = new_matrix[i, j+1]
            new_matrix[i, j+1] = 0
            l_neighbors += [puzzle_state(new_matrix, self.g + 1)]
        if j-1 >= 0:
            new_matrix = self.matrix.copy()
            new_matrix[i, j] = new_matrix[i, j-1]
            new_matrix[i, j-1] = 0
            l_neighbors += [puzzle_state(new_matrix, self.g + 1)]
        return l_neighbors

    def __eq__(self, other):
        if isinstance(other, puzzle_state):
            return np.array_equal(self.matrix, other.matrix)
        else: return False

    def __hash__(self):
        return hash(self.matrix.tostring())

    def __str__(self):
        return np.array2string(self.matrix)