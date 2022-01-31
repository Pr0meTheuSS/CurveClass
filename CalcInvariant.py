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
    logger = logging.GetLogger(__name__)
    # Create handler with file output
    file_handler = logging.FileHandler(__name__ + ".log")
    # Create formatter and add to handler
    formatter_str = '%(asc_time)s - %(level_name)s - %(filename)s - %(func_Name)s - %(line_no)s - %(msg)'
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
    # TODO: reshape doesn't work
    small_delta = np.linalg.det(coefficient_matrix.reshape((2, 2)))

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
