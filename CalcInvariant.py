from enum import Enum
import numpy as np
import logging


class ECurveClassType(Enum):
    Ellipse = 0
    ImagineEllipse = 1
    Hyperbola = 2
    Parabola = 3
    CrossedLines = 4
    ParallelLines = 5
    Point = 6


def CalcInvariant(coefficient_matrix):
    """
    Calculates all invariants and gets result as ECurveClassType variable 
    """
    # Logging part
    # Generate logger with name equal module name
    logger = logging.getLogger(__name__)
    logger.level = logging.DEBUG
    # Create handler with file output
    file_handler = logging.FileHandler('CalcInvariant' + ".log")
    # Create formatter and add to handler
    formatter_str = '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(msg)s'
    log_formatter = logging.Formatter(formatter_str)
    file_handler.setFormatter(log_formatter)
    # Add handler to logger
    logger.addHandler(file_handler)
    logger.info("Calc invariant module working")
    inv_type = 0
    s = coefficient_matrix[0][0] + coefficient_matrix[1][1]

    # Calc matrix det range == 3
    large_delta = np.linalg.det(coefficient_matrix)

    # Calc matrix det range == 2
    quadratic_form = coefficient_matrix[0:2, 0:2]
    # Division by 2 because in canonical form we have a1*x^2 + 2*b*x*y + ... = 0
    quadratic_form[1][0] = quadratic_form[0][1] = quadratic_form[0][1] / 2.0
    small_delta = np.linalg.det(quadratic_form)
    logger.debug("Quadratic form is:\n {q_form}".format(q_form=quadratic_form))
    logger.debug("Det of quadratic form is: {det}".format(det=small_delta))
    logger.debug("Calculated all invariants variable")

    # Chose compose of invariants to detect CurveType        
    if small_delta == 0:
        if large_delta != 0:
            inv_type = ECurveClassType.Parabola
        else:
            inv_type = ECurveClassType.ParallelLines
    elif small_delta < 0:
        if large_delta != 0:
            inv_type = ECurveClassType.Hyperbola
        else:
            inv_type = ECurveClassType.CrossedLines
    elif small_delta > 0:
        if large_delta != 0:
            if s * large_delta < 0:
                inv_type = ECurveClassType.Ellipse
            else:
                inv_type = ECurveClassType.ImagineEllipse
        else:
            inv_type = ECurveClassType.Point
    logger.debug("Detected curve type, all works done")
    return inv_type


if __name__ == '__main__':
    # 2x^2 - 2xy + 2y^2 - 5x - 3y + 10 = 0
    test_matrix = np.array([[2, -2, -5], [-2, 2, -3], [-5, -3, 10]])
    print(CalcInvariant(test_matrix))
