import nstargcm as gcm
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation
from classes import Star, Planet, System
import constants as con

if __name__ == "__main__":
    star1 = gcm.Star(name="Star 1", radius=1.4*con.rSun, mass=2*con.mSun, teff=8500, eccentricity=0., vel=[2,0,0], pos=[-5,0,0])
    star2 = gcm.Star(name="Star 2", radius=3*con.rSun,mass=5*con.mSun, teff=3300, eccentricity=0., vel=[0,0,0], pos=[0,0,0])
    star3 = gcm.Star(name="Star 3", radius=0.4*con.rSun,mass=0.5*con.mSun, teff=3000, eccentricity=0., vel=[1,0,0], pos=[0,10,0])
    planet = gcm.Planet(name = "Planet", mass=con.mEarth, albedo=0.2, radius=con.rEarth, eccentricity=0,heatCapacity=1e7, 
                        rotPeriod=con.day, vel=[0,4,0], pos=[0,11,0])
    system = gcm.System([star1,star2,star3,planet])
    gcm.calculateSystem(system=system, simTime=2*con.year, dt=3600)