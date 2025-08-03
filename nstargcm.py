import numpy as np
import helper_methods.gravitysimulation as gs
import helper_methods.interactionhandler as ih
import helper_methods.plotmethod as pm
import constants as con
from classes import Body, Star, Planet, System, SystemComponent
import logginghandler as log

def calculateStarParameters(star1 : Star, star2 : Star, axis : float) -> dict[float]:
    return {
        "period" : 2*np.pi*axis*(axis/(con.G*(star1.mass+star2.mass)))**0.5, 
        "star1Axis" : (star2.mass*axis)/(star1.mass+star2.mass), 
        "star2Axis" : (star1.mass*axis)/(star1.mass+star2.mass)
        }

def calculateBoundaries(positions, system):
    pos = positions.y[:3*system.componentNumber]
    min_coords = np.min(pos)
    max_coords = np.max(pos)
    padding = 0.1 * (max_coords - min_coords)
    xlim = [min_coords - padding, max_coords + padding]
    ylim = [min_coords - padding, max_coords + padding]
    zlim = [min_coords - padding, max_coords + padding]
    limits = [xlim, ylim, zlim]
    return limits
def calculateSystem(system : System, simTime : float, dt : float, doLogging : bool, filename : str):
    log.ENABLE_LOGGING = doLogging
    time = simTime/dt
    timeArray = np.linspace(0,simTime,int(simTime/dt))
    planet = system.getPlanet()
    stars = system.getStars()
    positions = gs.simulateSystem(system, simTime, timeArray)
    limits = calculateBoundaries(positions,system)
    system.positions = convertSimulation(positions, system)
    log.debugVariable("Positions", system.positions)
    system.distances = ih.calculateDistances(planet, stars, system.positions, time)
    log.debugVariable("Distances", system.distances)
    system.fluxes = ih.calculateFlux(planet, stars, system.distances, time)
    log.debugVariable("Fluxes", system.fluxes)
    pm.animateSystem(system, time, limits, filename, timeArray)
    pm.paramsOverTime(system,timeArray, filename)

def convertSimulation(positions, system : System):
    
    positions = positions.y[:3*system.componentNumber]
    
    trajectory_dict = {}
    for i, body in enumerate(system.components):
        body_name = body.name
        body_positions = positions[3*i:3*i+3].T 
        trajectory_dict[body_name] = body_positions
    return trajectory_dict
