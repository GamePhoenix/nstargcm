import numpy as np

class Body:
    def __init__(self, mass : float, pos : np.array, vel : np.array):
        self.mass = mass
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)

class Star(Body):
    def __init__(self, teff : int, mass : float, eccentricity : float,  vel : np.array,  pos : np.array) -> None:
        super().__init__(mass, pos, vel)
        self.teff = teff
        self.eccentricity = eccentricity

class Planet(Body):
    def __init__(self, albedo : float, mass : float, radius : float, eccentricity : float, 
                 heatCapacity : float, rotPeriod : float,  vel : np.array,  pos : np.array) -> None:
        super().__init__(mass, pos, vel)
        self.albedo = albedo
        self.radius = radius
        self.eccentricity = eccentricity
        self.heatCapacity = heatCapacity
        self.rotPeriod = rotPeriod

class System:
    def __init__(self, bodies : list[Body]):
        self.bodies = bodies