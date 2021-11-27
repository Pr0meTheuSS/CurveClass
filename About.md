# ABOUT UTILITY #
***CurveClass*** -

 module for __classification of plane curves of the second order__ 

*(and surfaces of the second order in perspective)*.

## Utility Workflows ##
1. takes as input a string representing the algebraic equation of a certain curve (surface) of the second order
2. determines its form
3. determines necessary transformations to bring it to the canonical form
4. graphically displays all data

## Utility Modules ##
- __CurveClass__ - initial main class, cintains all function modules
- __ParseAlgCurve__ - module for parsing coefficients for next modules *(if input invariant is violated - throw exception)*
- __CalcInvariant__ - module for calculating curves's invariant
- __CalcTransformations__ - module for calculating matrix tranfsformations to bring curve to the canonical form
- __Graphics__ - module for representing all information about curve *(or about some warnings and errors)* using Graphical Shell

### Utility Requirements ##
- Python with 3.x version
- Numpy for matrix and algebraic transformation
- Matplotlib for graphical displays at the later stages of the project

---

