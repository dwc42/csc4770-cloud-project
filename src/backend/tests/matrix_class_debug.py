from src.backend.matrix import Matrix
import numpy

m1 = Matrix(4, 4).randomizeInt((1, 10))
m2 = Matrix(4, 4).randomizeInt((1, 10))
print(m1)
print(m2)
split = m1.splitMatrix(3)

for i, part in enumerate(m1.splitMatrix(3)):
    print(i, "part", part)
    mul = part.multiply(m2)
    print(i, "mul", mul)

mul = [part.multiply(m2).matrix for part in split]
print(mul)

result = numpy.vstack(mul)
print("combined: ", result)
print("reg: ", m1.multiply(m2))
