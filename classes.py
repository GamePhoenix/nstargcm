import numpy as np
import constants as con

class Body:
    def __init__(self, name : str, mass : float, radius : float, pos : np.array, vel : np.array):
        self.mass = mass
        self.radius = radius
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.name = name
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Body) and self.name == other.name
    
class Star(Body):
    def __init__(self, name : str, teff : int, mass : float, radius : float, eccentricity : float, vel : np.array,  pos : np.array) -> None:
        super().__init__(name, mass, radius, pos, vel)
        self.teff = teff
        self.eccentricity = eccentricity
        self.luminosity = 4*np.pi*con.stefBolt*radius**2*teff**4

class Planet(Body):
    def __init__(self, name : str, albedo : float, mass : float, radius : float, eccentricity : float, 
                 heatCapacity : float, rotPeriod : float,  vel : np.array,  pos : np.array) -> None:
        super().__init__(name, mass, radius, pos, vel)
        self.albedo = albedo
        self.eccentricity = eccentricity
        self.heatCapacity = heatCapacity
        self.rotPeriod = rotPeriod

class System:
    def __init__(self, bodies : list[Body]):
        self.bodies = bodies
        self.positions = None
        self.distances = None
        self.fluxes = None
    def getPlanet(self) -> Planet:
        return next((body for body in self.bodies if isinstance(body, Planet)), None)
    def getStars(self) -> list[Star]:
        return[body for body in self.bodies if isinstance(body, Star)]