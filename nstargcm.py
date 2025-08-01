import numpy as np
from matplotlib.animation import FuncAnimation
import helper_methods.keplersolver as ks
import helper_methods.gravitysimulation as gs
from classes import Body, Star, Planet, System
import constants as con

def calculateStarParameters(star1 : Star, star2 : Star, axis : float) -> dict[float]:
    return {
        "period" : 2*np.pi*axis*(axis/(con.G*(star1.mass+star2.mass)))**0.5, 
        "star1Axis" : (star2.mass*axis)/(star1.mass+star2.mass), 
        "star2Axis" : (star1.mass*axis)/(star1.mass+star2.mass)
        }
   
def calculateSystem(system : System, simTime : float, dt : float):
    time = np.linspace(0, simTime, int(simTime/dt))
    positions = gs.simualteSystemPositions(system, simTime, dt)