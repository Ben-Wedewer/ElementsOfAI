import numpy as np

data = [[1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [1, 1, 1, 0, 1, 3, 0, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1]]

def find_nearest_pair(data):
    N = len(data)
    dist = np.empty((N, N), dtype=float)
    
    for i in range(N):
        for j in range(N):
            if i != j:
                sum_distance = sum(abs(data[i][k] - data[j][k]) for k in range(len(data[i])))
                dist[i][j] = sum_distance
            else:
                dist[i][j] = np.inf

    nearest_pair = np.unravel_index(np.argmin(dist), dist.shape)
    print(nearest_pair)

find_nearest_pair(data)
