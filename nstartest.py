import numpy as np
import matplotlib.pyplot as plt

class Body:
    def __init__(self, mass, pos, vel):
        self.mass = mass
        self.pos = np.array(pos, dtype=float)
        self.vel = np.array(vel, dtype=float)

def gravitational_force(b1, b2):
    G = 1
    r_vec = b2.pos - b1.pos
    r_mag = np.linalg.norm(r_vec)
    if r_mag == 0:
        return np.zeros(3)
    force_mag = G * b1.mass * b2.mass / r_mag**2
    force_vec = force_mag * r_vec / r_mag
    return force_vec

star = Body(1000, [0, 0, 0], [0, 0, 0])
planet = Body(1, [1, 0, 0], [0, 1, 0])

dt = 0.01
steps = 10000

star_positions = []
planet_positions = []

for _ in range(steps):
    f_on_star = gravitational_force(star, planet)
    f_on_planet = gravitational_force(planet, star)

    star.vel += f_on_star / star.mass * dt
    star.pos += star.vel * dt

    planet.vel += f_on_planet / planet.mass * dt
    planet.pos += planet.vel * dt

    star_positions.append(star.pos.copy())
    planet_positions.append(planet.pos.copy())

star_positions = np.array(star_positions)
planet_positions = np.array(planet_positions)

plt.figure(figsize=(6,6))
plt.plot(planet_positions[:,0], planet_positions[:,1], label='Planet Orbit')
plt.plot(star_positions[:,0], star_positions[:,1], label='Star Orbit')
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()
