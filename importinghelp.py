import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from astropy.constants import G, M_sun
from astropy import units as u

# === ORBITAL PARAMETERS ===
M_star = 1.0 * M_sun.value         # Mass of the star (kg)
a = 1.0 * u.AU.to('m')              # Semi-major axis (in meters)
e = 0.9                             # Eccentricity of the orbit

# Compute orbital period using Kepler's 3rd law
P = 2 * np.pi * np.sqrt(a**3 / (G.value * M_star))  # in seconds
print(f"Orbital period: {P / (3600*24):.2f} days")

# === TIME DOMAIN ===
num_frames = 500
t = np.linspace(0, P, num_frames)

# === SOLVE KEPLER'S EQUATION ===
def solve_kepler(M, e, tol=1e-8):
    E = M.copy()
    for _ in range(100):
        E_new = E - (E - e * np.sin(E) - M) / (1 - e * np.cos(E))
        if np.max(np.abs(E_new - E)) < tol:
            break
        E = E_new
    return E

# Mean anomaly
M = 2 * np.pi * t / P

# Eccentric anomaly
E = solve_kepler(M, e)

# True anomaly
theta = 2 * np.arctan2(np.sqrt(1 + e) * np.sin(E / 2),
                       np.sqrt(1 - e) * np.cos(E / 2))

# Orbital radius
r = a * (1 - e * np.cos(E))

# Cartesian coordinates
x = r * np.cos(theta)
y = r * np.sin(theta)

# === ANIMATION ===
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_aspect('equal')
ax.grid(True)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_xlabel("x (AU)")
ax.set_ylabel("y (AU)")
ax.set_title("Keplerian Orbit Animation (Star at Focus)")

orbit_line, = ax.plot([], [], 'b-', lw=1)
planet_dot, = ax.plot([], [], 'ro')
star_dot, = ax.plot([0], [0], 'yo', label="Star (focus)")

x_AU = x / u.AU.to('m')
y_AU = y / u.AU.to('m')

# Initialize plot
def init():
    orbit_line.set_data(x_AU, y_AU)
    planet_dot.set_data([], [])
    return orbit_line, planet_dot

# Update function for animation
def update(frame):
    planet_dot.set_data([x_AU[frame]], [y_AU[frame]])
    return planet_dot,

ani = FuncAnimation(fig, update, frames=num_frames,
                    init_func=init, blit=True, interval=30)

plt.legend()
plt.tight_layout()
plt.show()
