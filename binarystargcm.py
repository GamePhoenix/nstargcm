import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as astropyc
from matplotlib.animation import FuncAnimation
from astropy import units as u
import keplersolver as ks

class Star:
    def __init__(self, teff : int, mass : float, eccentricity : float) -> None:
        self.teff = teff
        self.mass = mass
        self.eccentricity = eccentricity
class Planet:
    def __init__(self, albedo : float, mass : float, distance : float, radius : float, eccentricity : float, heatCapacity : float, period : float) -> None:
        self.albedo = albedo
        self.mass = mass
        self.distance = distance
        self.radius = radius
        self.eccentricity = eccentricity
        self.heatCapacity = heatCapacity
        self.period = period

def calculateSystem(star1 : Star, star2 : Star, planet : Planet, axis : float, timeYears : int, steps : int) -> list[float]:
    params : dict[float] = calculateStarParameters(star1, star2, axis)
    time = np.linspace(0, timeYears, steps)
    for t in time:
        meanAnomaly = 2*np.pi*params["period"]/t
        eccentricAnomaly = ks.solveKepler(planet.eccentricity, meanAnomaly)

def calculateStarParameters(star1 : Star, star2 : Star, axis : float) -> dict[float]:
    return {
        "period" : 2*np.pi*axis*(axis/(astropyc.G*(star1.mass+star2.mass)))**0.5, 
        "star1Axis" : (star2.mass*axis)/(star1.mass+star2.mass), 
        "star2Axis" : (star1.mass*axis)/(star1.mass+star2.mass)
        }