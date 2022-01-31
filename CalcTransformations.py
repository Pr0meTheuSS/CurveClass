import numpy as np


def CalcTransformations(coefficient_matrix):
    """
  , curveInvariant
  Module for calculation move vector and rotation angle for 
  representation alg. curve into canonical form
  """
    # Extract submatrix
    A = coefficient_matrix[0:2, 0:2]
    # Make matrix for resolving symmetry center system
    A[0][0] *= 2
    A[1][1] *= 2
    A[1][0] = A[0][1]
    print("Matrix A:")
    print(A)
    B = coefficient_matrix[0:2, 2]
    print("Matrix B:")
    print(B)
    result = np.linalg.solve(A, B)
    print("Matrix result:")
    print(result)


# For tests
if __name__ == '__main__':
    # 2x^2 - 2xy + 2y^2 - 5x - 3y + 10 = 0
    test_matrix = np.array([[2, -2, -5], [-2, 2, -3], [-5, -3, 10]])
    CalcTransformations(test_matrix)
