import numpy as np
import helper_methods.keplersolver as ks
import helper_methods.gravitysimulation as gs
import helper_methods.interactionhandler as ih
import helper_methods.plotmethod as pm
import constants as con
from classes import Body, Star, Planet, System
import logginghandler as log

def calculateStarParameters(star1 : Star, star2 : Star, axis : float) -> dict[float]:
    return {
        "period" : 2*np.pi*axis*(axis/(con.G*(star1.mass+star2.mass)))**0.5, 
        "star1Axis" : (star2.mass*axis)/(star1.mass+star2.mass), 
        "star2Axis" : (star1.mass*axis)/(star1.mass+star2.mass)
        }
   
def calculateSystem(system : System, simTime : float, dt : float, doLogging : bool):
    log.ENABLE_LOGGING = doLogging
    time = simTime/dt
    timeArray = np.linspace(0,simTime,int(simTime/dt))
    planet = system.getPlanet()
    stars = system.getStars()
    system.positions = gs.simualteSystemPositions(system, simTime, dt)
    log.debugVariable("Positions", system.positions)
    system.distances = ih.calculateDistances(planet, stars, system.positions, time)
    log.debugVariable("Distances", system.distances)
    system.fluxes = ih.calculateFlux(planet, stars, system.distances, time)
    log.debugVariable("Fluxes", system.fluxes)
    pm.animateSystem(system, time)
    pm.paramsOverTime(system,timeArray)
    
