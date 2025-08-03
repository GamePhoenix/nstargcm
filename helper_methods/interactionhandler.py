import numpy as np
from classes import Star, Planet
import logginghandler as log
import time

def linearDistance(body1Pos : np.array, body2Pos : np.array) -> np.array:
    return np.linalg.norm(body1Pos-body2Pos)
def flux(luminosity : float, distance : float) -> float:
    return luminosity/(4*np.pi*distance**2)
def calculateDistances(planet : Planet, stars : list[Star], positions : dict, time):
    distances = {star.name : [] for star in stars}
    for t in range(int(time)):
        for star in stars:
            distances[star.name].append(linearDistance(positions[star.name][t],positions[planet.name][t]))
    return distances
#funny its so identical
def calculateFlux(planet : Planet, stars : list[Star], distances : dict, time : int):
    fluxes = {star.name : [] for star in stars}
    for t in range(int(time)):
        for star in stars:
            fluxes[star.name].append(flux(star.luminosity, distances[star.name][t]))
    return fluxes