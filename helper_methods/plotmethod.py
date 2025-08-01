import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time as timemodule
from classes import Star, Body, Planet, System
import constants as con
from mpl_toolkits.mplot3d import Axes3D


def update(frame, system: System, points, trails):
    for body in system.bodies:
        pos = system.positions[body][frame]
        trail = np.array(system.positions[body][:frame+1])

        points[body].set_data(pos[0], pos[1])
        points[body].set_3d_properties(pos[2])

        trails[body].set_data(trail[:, 0], trail[:, 1])
        trails[body].set_3d_properties(trail[:, 2])
    return list(points.values()) + list(trails.values())

def animateSystem(system : System, steps : int):
    limit = [-25*con.au, 25*con.au]
    fig = plt.figure()
    axis = fig.add_subplot(111,projection="3d")
    axis.set_xlim(limit)
    axis.set_ylim(limit)
    axis.set_zlim(limit)
    points = {}
    trails = {}
    for body in system.bodies:
        color = "yellow" if isinstance(body,Star) else "blue"
        (pt,) = axis.plot([],[],[], "o", color = color, label=body.name)
        (trail,) = axis.plot([],[],[], "-", color=color, alpha=0.5)
        points[body] = pt
        trails[body] = trail
    axis.legend()
    anim = FuncAnimation(fig, update, frames=int(steps), blit=False, interval=30, fargs=(system,points,trails))
    anim.save("SystemAnimation.gif", writer="pillow", fps=30)
    plt.show()


def paramsOverTime(system : System, timeArray):
    fig, axis = plt.subplots(2,1, figsize=(10,10), sharex=True)
    total_flux = np.sum([np.array(flux) for flux in system.fluxes.values()], axis=0)
    for star in system.getStars():
        axis[0].plot(timeArray, system.distances[star], label=f"Distance to {star.name}")
        axis[1].plot(timeArray, system.fluxes[star], label=f"Flux recieved from {star.name}")
    axis[1].plot(timeArray, total_flux, label="Total flux")
    axis[0].set_title("Distance and Flux over Time")
    axis[0].grid(True)
    axis[1].grid(True)
    plt.show()