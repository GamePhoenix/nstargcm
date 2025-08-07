import numpy as np
from scipy.special import roots_legendre
import sys
sys.path.insert(1, 'D:\piton\\Naukova')
import helpermethod.custommath as cm
from classes import Body, System

def gridCreate(resolution : int):
    lat, lon = resolution/21 * 32, resolution/21 * 64
    roots, _ = roots_legendre(2 * lat)
    latitudes = np.sort(np.degrees(np.arcsin(roots)))
    longitudes = np.linspace(0, 360, lon, endpoint=False)
    return latitudes, longitudes

def gridFlux(grid : np.array, positions, fluxes, system : System, time):
    lon, lat = grid[:, 0], grid[:, 1]
    x,y,z = np.cos(lon)*np.cos(lat), 
    np.sin(lon)*np.cos(lat),
    np.sin(lat)
    normals = np.stack([x,y,z], axis=1)
    recieved_flux = {star.name : [] for star in system.getStars()}
    for t in time:
        for star in system.getStars():

            recieved_flux[star.name].append()

point = np.array([-0.388969,-0.713177,0.584412])
print(point @ cm.rotationZ(cm.convertToRadians(90)) @ cm.rotationX(cm.convertToRadians(40)))  # Rotate a point counting in obliquity and time of day