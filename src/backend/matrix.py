import numpy
from numpy.typing import NDArray
from numpy.random import Generator


class Matrix:
    matrix: NDArray
    rng: Generator | None

    def __init__(self, mRows: int, nCols: int):
        self.matrix = numpy.zeros((mRows, nCols))
        self.rng = None

    @staticmethod
    def fromNDArray(ndArray: NDArray):
        [m, n] = ndArray.shape
        matrix = Matrix(n, m)
        matrix.matrix[:] = ndArray
        return matrix

    def initRNG(self):
        if self.rng is None:
            self.rng = numpy.random.default_rng()
        return self

    def randomizeFloat(self, range: tuple[float, float]):
        self.initRNG()
        self.matrix[:] = self.rng.uniform(range[0], range[1], size=self.matrix.shape)
        return self

    def randomizeInt(self, range: tuple[int, int]):
        self.initRNG()
        self.matrix[:] = self.rng.integers(
            low=range[0], high=range[1], size=self.matrix.shape
        )
        return self

    def multiply(self, m2: "Matrix") -> "Matrix":
        self.matrix = numpy.dot(self.matrix, m2.matrix)
        return self

    def __str__(self):
        return str(self.matrix)

    def __repr__(self):
        return str(self.matrix)


# m1 = Matrix(4, 4).randomizeInt((1, 10))
# m2 = Matrix(4, 4).randomizeInt((1, 10))
# print(m1)
# print(m2)

# print(m1.multiply(m2))
