import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time as timemodule
from classes import Star, Body, Planet, System
import constants as con
from mpl_toolkits.mplot3d import Axes3D
import math


def update(frame, system: System, points, trails, timeArray, time_text):
    for body in system.components:
        pos = system.positions[body.name][frame]
        trail = np.array(system.positions[body.name][:frame+1])

        points[body].set_data([pos[0]], [pos[1]])
        points[body].set_3d_properties([pos[2]])

        trails[body].set_data([trail[:, 0], trail[:, 1]])
        trails[body].set_3d_properties(trail[:, 2])

        current_time_years = timeArray[frame] / con.year
        time_text.set_text(f"t = {current_time_years:.2f} yr")

    return list(points.values()) + list(trails.values()) + [time_text]

def clamp(x, minimum=0, maximum=255):
    return max(minimum, min(maximum, x))

def getColor(T):
    T = T / 100.0

    red = 255 if T <= 66 else clamp(329.698727446 * (T - 60) ** -0.1332047592)
    green = 99.4708025861 * math.log(T) - 161.1195681661 if T <= 66 else clamp(288.1221695283 * (T - 60) ** -0.0755148492)
    if T >= 66:
        blue = 255
    elif T <= 19:
        blue = 0
    else:
        blue = 138.5177312231 * math.log(T - 10) - 305.0447927307
        blue = clamp(blue)

    return round(red/255,2), round(green/255, 2), round(blue/255,2)

def animateSystem(system : System, steps : int, limits, filename : str, timeArray):
    fig = plt.figure()
    axis = fig.add_subplot(111,projection="3d")
    time_text = fig.text(0.85, 0.95, "", fontsize=10) 
    axis.set_xlim(limits[0])
    axis.set_ylim(limits[1])
    axis.set_zlim(limits[2])
    points = {}
    trails = {}
    for body in system.components:
        color = getColor(body.teff) if isinstance(body, Star) else "black"
        (pt,) = axis.plot([],[],[], "o", color = color, label=body.name)
        (trail,) = axis.plot([],[],[], "-", color=color, alpha=0.5)
        points[body] = pt
        trails[body] = trail
    axis.legend()
    anim = FuncAnimation(fig, update, frames=int(steps), blit=False, interval=30, fargs=(system,points,trails, timeArray, time_text))
    anim.save(f"{filename}_animation.gif", writer="pillow", fps=30)
    plt.show()


def paramsOverTime(system : System, timeArray, filename : str):
    step = max(1, len(timeArray) // 500)
    fig, axis = plt.subplots(2,2, figsize=(10,10), sharex=True)
    total_flux = np.sum([np.array(flux) for flux in system.fluxes.values()], axis=0)
    for star in system.getStars():
        axis[0][0].plot(np.array(timeArray[::step])/con.year, np.array(system.distances[star.name][::step])/con.au, label=f"Distance to {star.name}"
                        , alpha=0.5)
        axis[1][0].plot(np.array(timeArray[::step])/con.year, np.array(system.fluxes[star.name][::step]), label=f"Flux recieved from {star.name}"
                        , alpha=0.5)
    axis[0][1].plot(np.array(timeArray)[::step]/con.year, np.array(total_flux)[::step], label="Total flux", alpha=0.5)

    axis[0][0].set_title("Distance over Time")
    axis[1][0].set_title("Flux over Time")
    axis[0][1].set_title("Total Flux over Time")

    axis[0][0].set_ylabel("Distance [a.u.]")
    axis[1][0].set_ylabel("Flux [W/m²]")
    axis[1][0].set_xlabel("Time [years]")
    axis[1][1].set_xlabel("Time [years]")
    axis[0][1].set_ylabel("Flux [W/m²]")

    axis[0][0].legend()
    axis[1][0].legend() 

    axis[0][0].grid(True)
    axis[1][0].grid(True)
    axis[0][1].grid(True)

    plt.savefig(f"{filename}_parameters.png")
    plt.show()