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
    eccentricAnomaly = solveKepler(e, meanAnomaly)
    return 2 * np.arctan2(np.sqrt(1+e) * np.sin(eccentricAnomaly/2),
                          np.sqrt(1-e) * np.cos(eccentricAnomaly/2))

def convertToRadians(angle):
    return angle * np.pi/180

def completeRotation(vector, longitudeAsc, inclination, periapsisArg):
    return rotationZ(longitudeAsc) @ rotationX(inclination) @ rotationZ(periapsisArg) @ vector

def rotationX(angle):
    return np.array([[1, 0, 0],
                    [0, np.cos(angle), -np.sin(angle)],
                    [0, np.sin(angle), np.cos(angle)]])

def rotationZ(angle):
    return np.array([[np.cos(angle), -np.sin(angle), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1]])
