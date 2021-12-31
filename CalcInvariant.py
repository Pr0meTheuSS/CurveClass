from enum import Enum
import numpy as np
import logging

class ECurveClassType(Enum):
    Ellipse
    ImagineEllipse
    Hyperbola
    Parabola
    CrossedLines
    ParallelLines
    Point


def CalcInvariant(coefficientsMatrix):
    """
    Calculates all invariants and gets result as ECurveClassType variable 
    """
    # Logging part
    # Genetrate logger with name equal module name
    logger = logging.GetLogger(__name__)
    # Create handler with file output
    file_handler = logging.FileHandler(__name__ + ".log")
    # Create formatter and add to handler
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(msg)')
    file_handler.setFormatter(log_formatter)
    # Add handler to logger
    logger.addHandler(file_handler)
    logger.info("Calc invariant module working")
    
    invariantType = 0

    s = coefficientsMatrix[0][0] + coefficientsMatrix[1][1] 

    # Calc matrix det range == 3
    largeDelta = np.linalg.det(coefficientsMatrix)
    
    # Calc matrix det range == 2    
    smallDelta = np.linalg.det(coefficientsMatrix.reshape((2, 2)))
    
    logger.debug("Calced all invariants variable")

    # Chose compose of invariants to detect CurveType        
    if smallDelta == 0:
        if largeDelta != 0:
            invariantType = ECurveClassType.Parabola
        else:
            invariantType = ECurveClassType.ParallelLines
    elif smallDelta < 0:
        if largeDelta != 0: 
            invariantType = ECurveClassType.Hyperbola
        else:
            invariantType = ECurveClassType.CrossedLines
    elif smallDelta > 0:
        if largeDelta != 0:
            if s * largeDelta < 0:
                invariantType = ECurveClassType.Ellipse
            else:
                invariantType = ECurveClassType.ImagineEllipse
        else:
            invariantType = ECurveClassType.Point
    logger.debug("Detected curve type, all works done")
    return invariantType
