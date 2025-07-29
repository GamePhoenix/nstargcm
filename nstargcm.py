import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as astropyc
from matplotlib.animation import FuncAnimation
from astropy import units as u

#First Push! 

class Star:
    def __init__(self, teff : int, mass : float) -> None:
        self.teff = teff
        self.mass = mass

class Planet:
    def __init__(self, albedo : float, mass : float, distance : float, radius : float, eccentricity : float, heatCapacity : float, period : float) -> None:
        self.albedo = albedo
        self.mass = mass
        self.distance = distance
        self.radius = radius
        self.eccentricity = eccentricity
        self.heatCapacity = heatCapacity
def calculateSystem(stars : list[Star] , planet : Planet, axis : float) -> list[float]:
    calculateStarParameters(stars, axis)
    calculateFluxOnPlanet()
def calculateFluxOnPlanet(stars : list[Star],planet : Planet) -> float:
    ... 
def calculateStarParameters(stars: list[Star], axis : float) -> list[float]:
    return[2*np.pi*axis*(axis/(astropyc.G*sum([star.mass for star in stars])))**0.5,]