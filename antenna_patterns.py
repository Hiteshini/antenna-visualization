# antenna_patterns.py
import numpy as np
import matplotlib.pyplot as plt

# Simple isotropic pattern in polar plot
def plot_isotropic_pattern():
    theta = np.linspace(0, 2 * np.pi, 360)
    r = np.ones_like(theta)
    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r)
    ax.set_title("Isotropic Antenna Pattern")
    plt.savefig("plots/polar_pattern.png")
    plt.close()

# Cosine-based directional pattern
def plot_directional_pattern():
    theta = np.linspace(0, 2 * np.pi, 360)
    r = np.abs(np.cos(theta))
    plt.figure()
    ax = plt.subplot(111, polar=True)
    ax.plot(theta, r)
    ax.set_title("Directional Antenna Pattern")
    plt.savefig("plots/directional_pattern.png")
    plt.close()

# 3D radiation pattern using spherical coordinates
def plot_3d_radiation_pattern():
    from mpl_toolkits.mplot3d import Axes3D

    theta = np.linspace(0, np.pi, 180)
    phi = np.linspace(0, 2 * np.pi, 360)
    theta, phi = np.meshgrid(theta, phi)

    r = np.abs(np.sin(theta))  # example pattern

    x = r * np.sin(theta) * np.cos(phi)
    y = r * np.sin(theta) * np.sin(phi)
    z = r * np.cos(theta)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z, cmap='viridis')
    ax.set_title("3D Radiation Pattern")
    plt.savefig("plots/3d_radiation_pattern.png")
    plt.close()

if __name__ == "__main__":
    plot_isotropic_pattern()
    plot_directional_pattern()
    plot_3d_radiation_pattern()
