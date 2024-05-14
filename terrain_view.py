import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualize_terrain(terrain):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    size = terrain.shape[0]
    x = np.linspace(0, 1, size)
    y = np.linspace(0, 1, size)
    x, y = np.meshgrid(x, y)
    ax.plot_surface(x, y, terrain, cmap='terrain')

    plt.show()

if __name__ == "__main__":
    terrain = np.load("terrain.npy")
    visualize_terrain(terrain)
