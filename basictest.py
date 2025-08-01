import nstargcm as gcm
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

def update(frame, planetPosList : np.array, starPosList : np.array):
    animated_plot_planet.set_data(planetPosList[:frame,0], planetPosList[:frame,1])
    animated_plot_planet.set_3d_properties(planetPosList[:frame,2])
    animated_plot_star.set_data(starPosList[:frame,0],starPosList[:frame,1])
    animated_plot_star.set_3d_properties(starPosList[:frame,2])
    return animated_plot_planet, animated_plot_star

if __name__ == "__main__":
    star = gcm.Star(teff=6000, mass=1000, eccentricity=0, vel=[5, 5, 0], pos=[0, 0, 0])
    planet = gcm.Planet(albedo=0.5, mass=100, radius=5, eccentricity=0,
                heatCapacity=1e7, period=1, vel=[0, 30, 0], pos=[1, 1, 1])

    simTime = 2
    dt = 0.001
    time = np.linspace(0, simTime, int(simTime/dt))
    starPosList, planetPosList = [star.initialPos.copy()],[planet.initialPos.copy()]
    for t in time:
        starForce = gcm.gravitationalForce(star,planet)
        planetForce = gcm.gravitationalForce(planet,star)
        star.pos += starForce/star.mass * dt
        star.initialPos += star.pos*dt
        starPosList.append(star.initialPos.copy())

        planet.pos += planetForce/planet.mass * dt
        planet.initialPos += planet.pos*dt
        planetPosList.append(planet.initialPos.copy())
    
    starPosList, planetPosList = np.array(starPosList),np.array(planetPosList)

    fig = plt.figure()
    axis = fig.add_subplot(111, projection="3d")

    axis.set_xlim([-3,20])
    axis.set_ylim([-3,20])
    axis.set_zlim([-3,20])

    animated_plot_star, = axis.plot([],[],[])
    animated_plot_planet, = axis.plot([],[],[])
    
    animation = FuncAnimation(
        fig=fig,
        func=update,
        frames=len(time),
        fargs=(planetPosList, starPosList),
        interval=25
    )
    animation.save("orbit_test.gif", writer="pillow", fps=30)
    plt.show()






    
