import numpy as np
def euclidean_distance(vec1, vec2):
    return np.linalg.norm(vec1 - vec2)

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

distance = euclidean_distance(a, b)
print("Euclidean distance:", distance)