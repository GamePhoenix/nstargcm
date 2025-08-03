import nstargcm as gcm
import matplotlib.pyplot as plt
import matplotlib.animation as FuncAnimation
import constants as con
import logginghandler as log

if __name__ == "__main__":
    star1 = gcm.Star(name="Star 1", radius=1.4*con.rSun, mass=2*con.mSun, teff=8500)
    star2 = gcm.Star(name="Star 2", radius=3*con.rSun,mass=5*con.mSun, teff=3300)
    star3 = gcm.Star(name="Star 3", radius=0.4*con.rSun,mass=0.5*con.mSun, teff=3000)
    planet = gcm.Planet(name="Planet", albedo=0.2, mass=con.mEarth, radius=con.rEarth, 
                 heatCapacity=1e7, rotPeriod=con.day)
    binaryStar = gcm.SystemComponent(compA=star1, compB=star2,  name="SubSystem AB", axis=6*con.au, 
                                     eccentricity=0.1, inclination=5., longitudeAsc=10, periapsisArg=80.)
    log.debugPosVel(binaryStar)
    planetComponent = gcm.SystemComponent(compA=star3, compB=planet,  name="SubSystem Cb", axis=1.5*con.au, 
                                     eccentricity=0.45, inclination=45., longitudeAsc=45., periapsisArg=0.)
    log.debugPosVel(planetComponent)
    system = gcm.System(binaryStar, planetComponent, axis=20*con.au, 
                                     eccentricity=0., inclination=0., longitudeAsc=0., periapsisArg=0.)
    log.debugPosVel(binaryStar)
    log.debugPosVel(planetComponent)
    gcm.calculateSystem(system=system, simTime=100*con.year, dt=0.1*con.year, doLogging=True, filename="averagesimtime")