import nstargcm as gcm
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation
import constants as con
import logginghandler as log
from classes import Star, Planet, SystemComponent, System

if __name__ == "__main__":
    star1 = Star(name="Star 1", radius=1.4*con.rSun, mass=2*con.mSun, teff=8500)
    star2 = Star(name="Star 2", radius=3*con.rSun,mass=5*con.mSun, teff=3300)
    star3 = Star(name="Star 3", radius=0.4*con.rSun,mass=0.5*con.mSun, teff=3000)
    planet = Planet(name="Planet", albedo=0.2, mass=con.mEarth, radius=con.rEarth, 
                 heatCapacity=1e7, rotPeriod=con.day, axialTilt=45.)
    binaryStar = SystemComponent(compA=star1, compB=star2,  name="SubSystem AB", axis=6*con.au, 
                                     eccentricity=0.1, inclination=5., longitudeAsc=10, periapsisArg=80.)
    planetComponent = SystemComponent(compA=star3, compB=planet,  name="SubSystem Cb", axis=1.5*con.au, 
                                     eccentricity=0.45, inclination=45., longitudeAsc=45., periapsisArg=0.)
    system = System(binaryStar, planetComponent, axis=20*con.au, 
                                     eccentricity=0., inclination=0., longitudeAsc=0., periapsisArg=0.)
    gcm.calculateSystem(system=system, simTime=20*con.year, dt=0.1*con.year, 
                        filename="newpathtest", anim=True, resolution=42)
