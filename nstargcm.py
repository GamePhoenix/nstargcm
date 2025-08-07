import numpy as np
import helpermethod.gravitysimulation as gs
import helpermethod.interactionhandler as ih
import helpermethod.plotmethod as pm
from classes import System, Body
import logginghandler as log
import time
import os
import datetime

def calculateBoundaries(positions, system : System):
    pos = positions.y[:3*system.componentNumber]
    min_coords = np.min(pos)
    max_coords = np.max(pos)
    padding = 0.1 * (max_coords - min_coords)
    xlim = [min_coords - padding, max_coords + padding]
    ylim = [min_coords - padding, max_coords + padding]
    zlim = [min_coords - padding, max_coords + padding]
    limits = [xlim, ylim, zlim]
    return limits
def calculateSystem(system : System, simTime : float, dt : float, filename : str, anim : bool,
                    resolution : int, frameSkip : int = 1 ):
    
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    simPath = os.path.join("simulations", f"{filename}-{timestamp}")
    outputPath = os.path.join(simPath, "output")
    os.makedirs(outputPath, exist_ok=True)

    logger = log.Logger(simPath)
    startTime = time.perf_counter()
    logger.simulation_start()

    framecount = simTime/dt
    timeArray = np.linspace(0,simTime,int(simTime/dt))
    planet = system.getPlanet()
    stars = system.getStars()

    logger.write("Setup is correct!")

    positions = gs.simulateSystem(system, simTime, timeArray)
    limits = calculateBoundaries(positions,system)
    system.positions = convertSimulation(positions, system)
    logger.write("Calculated positions")

    system.distances = ih.calculateDistances(planet, stars, system.positions, framecount)
    logger.write("Calculated distances")

    system.fluxes = ih.calculateFlux(planet, stars, system.distances, framecount)
    logger.write("Calculated fluxes")

    if anim:
        pm.animateSystem(system, framecount, frameSkip, limits, outputPath, timeArray)
        logger.write("Anims done")
    
    pm.paramsOverTime(system,timeArray, outputPath)
    logger.simulation_end(startTime, framecount)

def convertSimulation(positions, system : System):
    positions = positions.y[:3*system.componentNumber]
    trajectory_dict = {}
    for i, body in enumerate(system.components):
        body_name = body.name
        body_positions = positions[3*i:3*i+3].T 
        trajectory_dict[body_name] = body_positions
    return trajectory_dict
