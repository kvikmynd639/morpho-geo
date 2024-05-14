import numpy as np
from perlin_noise import PerlinNoise

def generate_perlin_noise(size, scale, octaves, seed=None):
    if seed:
        np.random.seed(seed)
    noise = PerlinNoise(octaves=octaves, seed=seed)
    noise_array = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            noise_array[i][j] = noise([i / scale, j / scale])
    return noise_array

if __name__ == "__main__":
    size = 100
    scale = 50.0
    octaves = 6
    seed = np.random.randint(0, 100)
    
    terrain = generate_perlin_noise(size, scale, octaves, seed)
    np.save("terrain.npy", terrain)
