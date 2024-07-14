import numpy as np

def tour_optimization(tour, distance_matrix):
    """Performs 2-opt optimization on the given tour."""
    n = len(distance_matrix)
    r = np.argsort(distance_matrix, axis=1)
    p = np.argsort(r, axis=1)
    y = np.argsort(tour)

    flag = True
    while flag:
        flag = False
        for i in range(n):
            n_ = p[tour[i], tour[(i + 1) % n]]
            for j_ in range(1, n_):
                j = y[r[tour[i], j_]]
                if i == j:
                    continue
                delta = (distance_matrix[tour[i], tour[j]] + distance_matrix[tour[(i + 1) % n], tour[(j + 1) % n]] - distance_matrix[tour[i], tour[(i + 1) % n]] - distance_matrix[tour[j], tour[(j + 1) % n]])
                if delta < 0:
                    if j < i:
                        i, j = j, i
                    tour[i + 1:j + 1] = tour[i + 1:j + 1][::-1]
                    y = np.argsort(tour)
                    flag = True

    return tour