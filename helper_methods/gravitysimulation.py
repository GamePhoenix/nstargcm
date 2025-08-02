import numpy as np
from classes import Body, System
import constants as con
import logginghandler as log
import time
import keplersolver as ks

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

def initiatingParams(systemComponents : list[Body]):
    for systemComponent in systemComponents:
        trueAnomaly = ks.solveTrueAnomaly(systemComponent.eccentricity, 0)
        distance = systemComponent.axis * (1-systemComponent.eccentricity**2) / 1+systemComponent.eccentricity * np.cos(trueAnomaly)
        rVec = np.array([0, distance, 0])
        velVec = np.array([0, np.sqrt(con.G*systemComponent.mass*(1/systemComponent.axis)*(1 + systemComponent.eccentricity / 1 - systemComponent.eccentricity)), 0])
        rVecPrime = completeRotation(rVec, systemComponent.longitudeAsc, systemComponent.inclination, systemComponent.periapsisArg)
        velVecPrime = completeRotation(velVec, systemComponent.longitudeAsc, systemComponent.inclination, systemComponent.periapsisArg)
        return [rVecPrime, velVecPrime]
        
def completeRotation(vector,longitudeAsc, inclination, periapsisArg):
    return vector @ rotationZ(longitudeAsc) @ rotationX(inclination) @ rotationZ(periapsisArg)

def rotationX(angle):
    return np.array([1, 0, 0],
                    [0, np.cos(angle), -np.sin(angle)],
                    [0, np.sin(angle), np.cos(angle)])

def rotationZ(angle):
    return np.array([np.cos(angle), -np.sin(angle), 0],
                    [np.sin(angle), np.cos(angle), 0],
                    [0, 0, 1])

def gravitationalForce(p1 : Body, p2 : Body) -> np.array:
    G = con.G
    disVec = p2.pos-p1.pos
    disMag = np.linalg.norm(disVec)
    return G*p1.mass*p2.mass/(disMag**2) * disVec/disMag if disMag != 0 else np.zeros(3, dtype=float)
 