import numpy as np
from classes import Body, System
import constants as con

def simualteSystemPositions(system : System, simTime : float, dt : float) -> dict[Body, list[np.array]]:
    positions = {body: [body.pos.copy()] for body in system.bodies}
    velocities = {body: body.vel.copy() for body in system.bodies}
    for _ in range(int(simTime/dt)):
        forces = {body : np.zeros(3) for body in system.bodies}
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
    return positions

def gravitationalForce(p1 : Body, p2 : Body) -> np.array:
    G = con.G
    disVec = p2.pos-p1.pos
    disMag = np.linalg.norm(disVec)
    return G*p1.mass*p2.mass/(disMag**2) * disVec/disMag if disMag != 0 else np.zeros_like(disVec)
 