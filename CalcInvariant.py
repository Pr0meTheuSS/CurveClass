from enum import Enum
import numpy as np


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
    invariantType = 0

    s = coefficientsMatrix[0][0] + coefficientsMatrix[1][1] 
    # Calc matrix det range == 3
    largeDelta = np.linalg.det(coefficientsMatrix)
    # Calc matrix det range == 2
    smallDelta = np.linalg.det(coefficientsMatrix.reshape((2, 2)))
    # Chose compose of invariants to detect CurveType    
    if smallDelta == 0:
        if largeDelta != 0:
            invariantType = Parabola
        else:
            invariantType = ParallelLines
    elif smallDelta < 0:
        if largeDelta != 0: 
            invariantType = Hyperbola
        else:
            invariantType = CrossedLines
    elif smallDelta > 0:
        if largeDelta != 0:
            if s * largeDelta < 0:
                invariantType = Ellipse
            else:
                invariantType = ImagineEllipse
        else:
            invariantType = Point
    return invariantType

