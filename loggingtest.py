import nstargcm as gcm
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation
from classes import Star, Planet, System
import constants as con

if __name__ == "__main__":
    star1 = gcm.Star(name="Star 1", radius=1.4*con.rSun, mass=2*con.mSun, teff=8500, eccentricity=0., vel=[0,4e4,0], pos=[-6*con.au,0,0])
    star2 = gcm.Star(name="Star 2", radius=3*con.rSun,mass=5*con.mSun, teff=3300, eccentricity=0., vel=[0,0,0], pos=[0,0,0])
    star3 = gcm.Star(name="Star 3", radius=0.4*con.rSun,mass=0.5*con.mSun, teff=3000, eccentricity=0., vel=[0,1e4,0], pos=[con.au,10*con.au,con.au])
    planet = gcm.Planet(name = "Planet", mass=con.mEarth, albedo=0.2, radius=con.rEarth, eccentricity=0,heatCapacity=1e7, 
                        rotPeriod=con.day, vel=[1e4,0,0], pos=[2*con.au,11*con.au,con.au])
    system = gcm.System([star1,star2,star3,planet])
    gcm.calculateSystem(system=system, simTime=10*con.year, dt=5*con.day, doLogging=True)