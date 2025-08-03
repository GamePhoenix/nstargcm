import nstargcm as gcm
import constants as con

if __name__ == "__main__":
    kepler16A = gcm.Star(name="Kepler-16A", teff=4450, mass=0.704*con.mSun, radius=0.6489*con.rSun,)
    kepler16B = gcm.Star(name="Kepler-16B", teff=3311, mass=0.2054*con.mSun, radius=0.22623*con.rSun)
    kepler16b = gcm.Planet(name="Kepler-16b", albedo=0.25, mass=0.33*con.mJup, radius=0.7538*con.rJup,
                           heatCapacity=1e7,rotPeriod=con.day)
    keplerStars = gcm.SystemComponent(name="Kepler Stars", compA=kepler16A, compB=kepler16B, axis=0.2257*con.au, eccentricity=0.15962,
                                      inclination=90.3, longitudeAsc=0, periapsisArg=263.67)
    kepler16System = gcm.System(compA=keplerStars, compB=kepler16b, axis=0.7048*con.au, eccentricity=0.0069,
                                inclination=90.032,longitudeAsc=0,periapsisArg=318)
    gcm.calculateSystem(kepler16System, 10*con.year, 10*con.day, True, "kepler-16")