import numpy as np
import random
import string
from Parser import ParseCoefficient


# TODO: rebuild like fixture
def CreateValidIntTestForParser(matrix: np.array) -> str:
    # Generate random variable's names
    var_names = [random.choice(string.ascii_letters), random.choice(string.ascii_letters)]
    # If names are the same
    while var_names[1] == var_names[0]:
        var_names[1] = random.choice(string.ascii_letters)
    return '{a11}{x2} + {a12}{xy} + {a22}{y2} + {a13}{x} + {a23}{y} + {a33}'.format(a11=matrix[0][0],
                                                                                    a12=matrix[1][0],
                                                                                    a22=matrix[1][1],
                                                                                    a13=matrix[0][2],
                                                                                    a23=matrix[1][2],
                                                                                    a33=matrix[2][2],
                                                                                    x2=var_names[0] + '^2',
                                                                                    xy=var_names[0] + var_names[1],
                                                                                    y2=var_names[1] + '^2',
                                                                                    x=var_names[0],
                                                                                    y=var_names[1])


# TODO: rebuild within fixture
def test_valid_input_parser():
    # Generate random symmetry matrix 3x3
    c_matrix: np.array = np.random.randint(-1000, 1000, size=(3, 3))
    for i in range(len(c_matrix)):
        for j in range(len(c_matrix[0])):
            c_matrix[i][j] = c_matrix[j][i]
    test_in: str = CreateValidIntTestForParser(c_matrix)
    answer: np.array = ParseCoefficient(test_in)
    assert np.array_equal(c_matrix, answer), 'Module parser failed with wrong answer'
