import nstargcm as gcm
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation
from classes import Star, Planet, System
import constants as con

if __name__ == "__main__":
    star1 = gcm.Star(mass=2*con.mSun, teff=8500, eccentricity=0., vel=[2,0,0], pos=[-5,0,0])
    star2 = gcm.Star(mass=5*con.mSun, teff=3300, eccentricity=0., vel=[0,0,0], pos=[0,0,0])
    star3 = gcm.Star(mass=0.5*con.mSun, teff=3000, eccentricity=0., vel=[1,0,0], pos=[0,10,0])
    planet = gcm.Planet(mass=con.mEarth, albedo=0.2, radius=con.rEarth, eccentricity=0,heatCapacity=1e7, 
                        rotPeriod=con.day, vel=[0,4,0], pos=[0,11,0])
    system = gcm.System([star1,star2,star3,planet])
    print(gcm.calculateSystem(system=system, simTime=con.year, dt=1))