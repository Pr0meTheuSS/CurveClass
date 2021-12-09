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


class CalcInvariant():
    """
    class description
    """
    
    
    def __init__(coeffMatrix):
    """
    Constructor
    """
        self.CoefficientsMatrix = coeffMatrix
    

    def GetInvariant():
    """
    Calculates all invariants and gets result as ECurveClassType variable 
    """
        s = self.CoefficientsMatrix[0][0] + self.CoefficientsMatrix[1][1] 
        # Calc matrix det range == 3
        largeDelta = np.linalg.det(self.CoefficientsMatrix)
        # Calc matrix det range == 2
        smallDelta = np.linalg.det(self.CoefficientsMatrix.reshape((2, 2)))
        # Chose compose of invariants to detect CurveType    
        if smallDelta == 0:
            if largeDelta != 0:
                self.InvariantType = Parabola
            else:
                self.InvariantType = ParallelLines
        elif smallDelta < 0:
            if largeDelta != 0: 
                self.InvariantType = Hyperbola
            else:
                self.InvariantType = CrossedLines
        elif smallDelta > 0:
            if largeDelta != 0:
                if s * largeDelta < 0:
                    self.InvariantType = Ellipse
                else:
                    self.InvariantType = ImagineEllipse
            else:
                self.InvariantType = Point


