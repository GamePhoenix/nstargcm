import numpy as np
import constants as con
from helper_methods.keplersolver import solveTrueAnomaly, completeRotation

def unpackBody(body):
    if isinstance(body, SystemComponent):
        bodies_a = unpackBody(body.compA)
        bodies_b = unpackBody(body.compB)
        return bodies_a + bodies_b
    else:
        return [body]
    

class Body:
    def __init__(self, name : str, mass : float, pos : np.array, vel : np.array):
        self.mass = mass
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)
        self.name = name
    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return isinstance(other, Body) and self.name == other.name

class Star(Body):
    def __init__(self, name : str, teff : int, mass : float, radius : float) -> None:
        super().__init__(name, mass, np.zeros_like(3, dtype=float), np.zeros_like(3, dtype=float))
        self.radius = radius
        self.teff = teff
        self.luminosity = 4*np.pi*con.stefBolt*radius**2*teff**4

class Planet(Body):
    def __init__(self, name : str, albedo : float, mass : float, radius : float, 
                 heatCapacity : float, rotPeriod : float) -> None:
        super().__init__(name, mass, np.zeros_like(3, dtype=float), np.zeros_like(3, dtype=float))
        self.radius = radius
        self.albedo = albedo
        self.heatCapacity = heatCapacity
        self.rotPeriod = rotPeriod

class SystemComponent(Body):
    def __init__(self, compA : Body, compB : Body,  name : str, axis : float, eccentricity : float, inclination : float, longitudeAsc : float, periapsisArg : float):
        super().__init__(name, compA.mass+compB.mass, np.zeros(3, dtype=float), np.zeros(3, dtype=float))
        self.eccentricity = eccentricity
        self.axis = axis
        self.order = None
        self.reducedMass = compA.mass*compB.mass / self.mass
        self.compA = compA
        self.compB = compB
        self.inclination = inclination
        self.longitudeAsc = longitudeAsc
        self.periapsisArg = periapsisArg
        self.initiatingParams()
    def initiatingParams(self):
        trueAnomaly = solveTrueAnomaly(self.eccentricity, 0)
        distance = self.axis * (1-self.eccentricity**2) / (1+self.eccentricity * np.cos(trueAnomaly))
        rVec = np.array([0, distance, 0])
        velVec = np.array([np.sqrt(con.G*self.mass*(1 + self.eccentricity) / (self.axis*(1 - self.eccentricity))), 0, 0])
        rVecPrime = completeRotation(rVec, self.longitudeAsc, self.inclination, self.periapsisArg)
        velVecPrime = completeRotation(velVec, self.longitudeAsc, self.inclination, self.periapsisArg)
        self.compA.pos =  -self.reducedMass/self.compA.mass * rVecPrime
        self.compB.pos =  self.reducedMass/self.compB.mass * rVecPrime
        self.compA.vel =  -self.reducedMass/self.compA.mass * velVecPrime
        self.compB.vel =  self.reducedMass/self.compB.mass * velVecPrime
        self.pos = (self.compA.mass * self.compA.pos + self.compB.mass * self.compB.pos) / self.mass
        self.pos = (self.compA.mass * self.compA.vel + self.compB.mass * self.compB.vel) / self.mass

def collectComponents(body: Body, current_order: int = 0) -> list[tuple[SystemComponent, int]]:
    if isinstance(body, SystemComponent):
        results = [(body, current_order)]
        results += collectComponents(body.compA, current_order + 1)
        results += collectComponents(body.compB, current_order + 1)
        return results
    else:
        return []

class System:
    def __init__(self, compA : Body, compB : Body):
        self.bodies = [compA, compB]
        self.positions = None
        self.distances = None
        self.fluxes = None
    def getBodies(self) -> None:
        all_bodies = []
        for body in self.bodies:
            all_bodies.extend(unpackBody(body))
        self.bodies = all_bodies
        return all_bodies
    def getPlanet(self) -> Planet:
        return next((body for body in self.getBodies() if isinstance(body, Planet)), None)
    def getStars(self) -> list[Star]:
        return[body for body in self.getBodies() if isinstance(body, Star)]
    def getSystemComponentsWithOrder(self) -> list[tuple[SystemComponent, int]]:
        all_components = []
        for body in self.bodies:
            all_components.extend(collectComponents(body))
        return all_components