import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as astropyc
from matplotlib.animation import FuncAnimation
from astropy import units as u
import keplersolver as ks
import vector as v

class Body:
    pass

class Star(Body):
    def __init__(self, teff : int, mass : float, eccentricity : float,  initialVel : np.array,  initialPos : np.array) -> None:
        self.teff = teff
        self.mass = mass
        self.eccentricity = eccentricity
        self.initialVel = np.array(initialVel, dtype=float) 
        self.initialPos = np.array(initialPos, dtype=float)

class Planet(Body):
    def __init__(self, albedo : float, mass : float, radius : float, eccentricity : float, 
                 heatCapacity : float, rotPeriod : float,  initialVel : np.array,  initialPos : np.array) -> None:
        self.albedo = albedo
        self.mass = mass
        self.radius = radius
        self.eccentricity = eccentricity
        self.heatCapacity = heatCapacity
        self.rotPeriod = rotPeriod
        self.initialVel = np.array(initialVel, dtype=float) 
        self.initialPos = np.array(initialPos, dtype=float)

class System:
    def __init__(self):
        pass

def calculateStarParameters(star1 : Star, star2 : Star, axis : float) -> dict[float]:
    return {
        "period" : 2*np.pi*axis*(axis/(astropyc.G*(star1.mass+star2.mass)))**0.5, 
        "star1Axis" : (star2.mass*axis)/(star1.mass+star2.mass), 
        "star2Axis" : (star1.mass*axis)/(star1.mass+star2.mass)
        }
def gravitationalForce(p1 : Body, p2 : Body) -> np.array:
    G = 1
    disVec = p2.initialPos-p1.initialPos
    disMag = np.linalg.norm(disVec)
    return G*p1.mass*p2.mass/(disMag**2) * disVec/disMag
    