import numpy as np

def keplerEquation(M : float, e : float, E : float) -> float:
    return E - e*np.sin(E) - M

def keplerDerivative(e : float, E : float) -> float:
    return 1 - e*np.cos(E)

def solveKepler(e : float, meanAnomaly : float) -> float:
    #Snippets of code from https://www.johndcook.com/blog/2022/11/02/keplers-equation-python/
    meanAnomaly = np.mod(meanAnomaly, 2*np.pi)
    eccentricAnomaly : float  = meanAnomaly
    tolerance = 1e-10
    while abs(keplerEquation(meanAnomaly,e,eccentricAnomaly))> tolerance:
        eccentricAnomaly -= keplerEquation(meanAnomaly,e,eccentricAnomaly)/keplerDerivative(e, eccentricAnomaly)
    return eccentricAnomaly

def solveTrueAnomaly(e : float, meanAnomaly : float):
    #Snippets of code from https://www.johndcook.com/blog/2022/11/02/keplers-equation-python/
    meanAnomaly = np.mod(meanAnomaly, 2*np.pi)
    eccentricAnomaly : float  = meanAnomaly
    tolerance = 1e-10
    while abs(keplerEquation(meanAnomaly,e,eccentricAnomaly))> tolerance:
        eccentricAnomaly -= keplerEquation(meanAnomaly,e,eccentricAnomaly)/keplerDerivative(e, eccentricAnomaly)
    return 2 * np.arctan2(np.sqrt(1+e) * np.sin(eccentricAnomaly/2),
                          np.sqrt(1-e) * np.cos(eccentricAnomaly/2))