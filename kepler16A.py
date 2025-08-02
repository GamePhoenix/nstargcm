import nstargcm as gcm
import constants as con

if __name__ == "__main__":
    kepler16A = gcm.Star(name="Kepler-16A", teff=4450, mass=0.704*con.mSun, radius=0.6489*con.rSun,
                         eccentricity=0.15962, pos=[0,0,0],vel=[13.5e3, 0,0])
    kepler16B = gcm.Star(name="Kepler-16B", teff=3311, mass=0.2054*con.mSun, radius=0.22623*con.rSun,
                         eccentricity=0.15962, pos=[0,-0.2257*(1+0.15962)*con.au,0],vel=[46e3, 0,0])
    kepler16b = gcm.Planet(name="Kepler-16b", albedo=0.25, mass=0.33*con.mJup, radius=0.7538*con.rJup,
                           eccentricity=0.0069,heatCapacity=1e7,rotPeriod=con.day, vel=[0,33.4e3,0],pos=[0.7048*con.au,0,0])
    kepler16System = gcm.System([kepler16A,kepler16B,kepler16b])
    gcm.calculateSystem(kepler16System, 2 *con.year, con.day, True, "kepler-16")