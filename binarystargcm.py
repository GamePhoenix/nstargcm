import numpy as np
import matplotlib.pyplot as plt
import astropy.constants as astropyc
from matplotlib.animation import FuncAnimation
from astropy import units as u
from enum import Enum

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

def calculateSystem(star1 : Star, star2 : Star, planet : Planet, axis : float) -> list[float]:
    params : dict[float] = calculateStarParameters(star1, star2, axis)
    period = params["period"]
    star1_axis = params["star1_axis"]
    star2_axis = params["star2_axis"]
    calculateFluxOnPlanet()
def calculateFluxOnPlanet(star1 : Star, star2 : Star, params,planet : Planet) -> float:
    ...
def calculateStarParameters(star1 : Star, star2 : Star, axis : float) -> dict[float]:
    return {
        "period" : 2*np.pi*axis*(axis/(astropyc.G*(star1.mass+star2.mass)))**0.5, 
        "star1_axis" : (star2.mass*axis)/(star1.mass+star2.mass), 
        "star2_axis" : (star1.mass*axis)/(star1.mass+star2.mass)
        }