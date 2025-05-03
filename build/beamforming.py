# beamforming.py
import numpy as np
import matplotlib.pyplot as plt

def plot_beamforming(N=8, d=0.5, theta0=30):
    theta = np.linspace(-90, 90, 1000)
    theta_rad = np.deg2rad(theta)
    theta0_rad = np.deg2rad(theta0)

    beta = 2 * np.pi * d * (np.sin(theta_rad) - np.sin(theta0_rad))
    AF = np.abs(np.sum(np.exp(1j * np.outer(np.arange(N), beta)), axis=0)) ** 2
    AF = AF / np.max(AF)  # normalize

    plt.figure()
    plt.plot(theta, AF)
    plt.title(f\"Beamforming Pattern (N={N}, Steering Angle={theta0}°)\")
    plt.xlabel(\"Angle (°)\")
    plt.ylabel(\"Normalized Array Factor\")
    plt.grid(True)
    plt.savefig(\"plots/beamforming_output.png\")
    plt.close()

if __name__ == \"__main__\":
    plot_beamforming()
