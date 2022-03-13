import numpy as np
import math as math


def det(matrix):
    return np.linalg.det(matrix)


def get_curve_name(curve_type):
    curve_name = "Not found :("
    match curve_type:
        case 1:
            curve_name = "Real ellipse"
        case 2:
            curve_name = "Point or pair complex lines"
        case 3:
            curve_name = "Complex ellipse"
        case 4:
            curve_name = "Hyperbola"
        case 5:
            curve_name = "Pair of intersecting lines"
        case 6:
            curve_name = "Parabola"
        case 7:
            curve_name = "Pair of parallel lines"
        case 8:
            curve_name = "Line"
        case 9:
            curve_name = "Pair of complex parallel lines"
    return curve_name


def calc_transformations(coefficient_matrix):
    """
    curveInvariant
    Module for calculation move vector and rotation angle for
    representation alg. curve into canonical form
    """
    # i3_matrix ~ coefficient_matrix
    i2_matrix = []
    rotate_matrix1 = []
    rotate_matrix2 = []
    for i in range(2):
        i2_matrix.append([0] * 2)
        rotate_matrix1.append([0] * 2)
        rotate_matrix2.append([0] * 2)
    # todo change to construction [0 : 2, 0 : 2]
    for i in range(2):
        for j in range(2):
            i2_matrix[i][j] = coefficient_matrix[i][j]
    # ~~~~~~~~
    i3_det = det(coefficient_matrix)
    i2_det = det(i2_matrix)
    i2_tr = i2_matrix[0][0] + i2_matrix[1][1]
    # it's invariant use for calc two matrix det.
    # first rotate matrix
    rotate_matrix1[0][0] = coefficient_matrix[0][0]
    rotate_matrix1[0][1] = coefficient_matrix[0][2]
    rotate_matrix1[1][0] = coefficient_matrix[0][2]
    rotate_matrix1[1][1] = coefficient_matrix[2][2]
    # second rotate matrix
    rotate_matrix2[0][0] = coefficient_matrix[1][1]
    rotate_matrix2[0][1] = coefficient_matrix[1][2]
    rotate_matrix2[1][0] = coefficient_matrix[1][2]
    rotate_matrix2[1][1] = coefficient_matrix[2][2]
    # invariant for check curve rotate
    i4_rotate = det(rotate_matrix1) + det(rotate_matrix2)
    curve_type = -1
    # i3_det = I3, i2_det = I2 , i2_tr = I1
    # curve types:
    # 1 - ellipse
    # 2 - point
    # 3 - complex ellipse
    # etc Check method get_curve_name(curve_type)
    if i2_det != 0:
        if i2_det > 0:
            if i2_tr * i3_det < 0:
                curve_type = 1
            elif i2_tr == 0:
                curve_type = 2
            elif i2_tr * i3_det > 0:
                curve_type = 3
        else:
            if i3_det != 0:
                curve_type = 4
            else:
                curve_type = 5
    else:
        if i3_det != 0:
            curve_type = 6
        else:
            if i4_rotate < 0:
                curve_type = 7
            elif i4_rotate == 0:
                curve_type = 8
            else:
                curve_type = 9
    # Calc curve rotate angle
    # I'm use fact: ctg(2Ф) = (a11 - a22) / 2a12, for Ф - rotate angle
    # And use trigonometry fact for too correct result: tg(pi/2 - 2Ф) = ctg(2Ф) => 2Ф = pi/2 - arctg(ctg(2Ф))
    ctg_rotate_angle = (coefficient_matrix[0][0] - coefficient_matrix[1][1]) / (2 * coefficient_matrix[0][1])
    rotate_angle = (math.acos(-1) / 2 - math.atan(ctg_rotate_angle)) / 2
    print("You curve have rotate angle: " + str(rotate_angle) + " rad. or " + str(
        rotate_angle * 180 / math.acos(-1)) + " degrees")
    print("Curve type is " + get_curve_name(curve_type))


# For tests
if __name__ == '__main__':
    # print("Module no init.")
    # 2x^2 - 2xy + 2y^2 - 5x - 3y + 10 = 0
    # Curve f: R x R -> R, f(x, y) = a11x^2 + 2a12xy + a22y^2 + 2a13x + 2a23y + a33
    # Template matrix
    # First row: [a11, a12, a13]
    # Second row: [a12, a22, a23]
    # third row: [a13, a23, a33]
    # test_matrix = np.array([[2, -2, -5], [-2, 2, -3], [-5, -3, 10]])

    # For test I use curve 13x^2 - 10xy + 13y^2 - 72 = 0
    test_matrix = []
    for i in range(3):
        test_matrix.append([0] * 3)
    test_matrix[0][0] = 13
    test_matrix[0][1] = -5
    test_matrix[0][2] = 0
    test_matrix[1][0] = -5
    test_matrix[1][1] = 13
    test_matrix[1][2] = 0
    test_matrix[2][0] = 0
    test_matrix[2][1] = 0
    test_matrix[2][2] = -72
    calc_transformations(test_matrix)
