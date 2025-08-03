import numpy as np
from classes import Body, System
import constants as con
import logginghandler as log
import time
import helper_methods.custommath as ks
from scipy.integrate import solve_ivp

@DeprecationWarning
def simualteSystemPositions(system : System, simTime : float, dt : float) -> dict[Body, list[np.array]]:
    total = simTime/dt
    startTime = time.perf_counter()
    log.simulation_start()
    positions = {body: [body.pos.copy()] for body in system.bodies}
    velocities = {body: body.vel.copy() for body in system.bodies}
    for k in range(int(total)):
        frameStart = time.perf_counter()
        forces = {body : np.zeros(3, dtype=float) for body in system.bodies}
        for i, body1 in enumerate(system.bodies):
            for j in range(i+1, len(system.bodies)):
                body2 = system.bodies[j]
                force = gravitationalForce(body1, body2)
                forces[body1] += force
                forces[body2] -= force
        for body in system.bodies:
            velocities[body] += forces[body]/body.mass * dt
            body.pos += velocities[body] * dt
            positions[body].append(body.pos.copy())
        log.performance(k, total, frameStart)
    log.simulation_end(startTime, total)
    return positions

@DeprecationWarning
def gravitationalForce(p1 : Body, p2 : Body) -> np.array:
    G = con.G
    disVec = p2.pos-p1.pos
    disMag = np.linalg.norm(disVec)
    return G*p1.mass*p2.mass/(disMag**2) * disVec/disMag if disMag != 0 else np.zeros(3, dtype=float)

def getDerivatives(t : float, y : np.ndarray, system : System):
    pos = y[:3*system.componentNumber].reshape((system.componentNumber,3))
    vel = y[3*system.componentNumber:].reshape((system.componentNumber,3))
    acceleration = np.zeros((system.componentNumber,3), dtype=float)

    for i, body_i in enumerate(system.components):
        for j, body_j in enumerate(system.components):
            if i == j:
                continue
            distanceVec = pos[j] - pos[i]
            distanceMag = np.sqrt(np.sum(distanceVec**2)) + 1e-10
            acceleration[i] += system.components[j].mass * distanceVec/distanceMag**3
    
    dydt = np.concatenate((vel, acceleration * con.G), axis=0)
    return dydt.flatten()

def simulateSystem(system : System, simTime : float, timeArray):
    tol = 1e-9
    initialComps = system.combineInitialParams()
    return solve_ivp(fun = lambda t, y: getDerivatives(t, y, system),
                    t_span=(0,simTime),
                    y0=initialComps,
                    t_eval=timeArray,
                    rtol=tol, 
                    atol=tol
                    )


 