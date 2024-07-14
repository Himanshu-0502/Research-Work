import numpy as np

def read_tsp_coordinates(filename):
    """Reads TSP coordinates from a file."""
    coordinates = []
    with open(filename, 'r') as file:
        for line in file:
            if line.strip() == 'EOF':
                break
            if line.strip() == 'NODE_COORD_SECTION':
                break
        for line in file:
            if line.strip() == 'EOF':
                break
            i, x, y = line.strip().split()
            coordinates.append((float(x), float(y)))
    return np.array(coordinates)

def create_distance_matrix(coordinates):
    """Creates a distance matrix from coordinates."""
    return np.array([[int(np.linalg.norm(c1 - c2)) for c2 in coordinates] for c1 in coordinates])

def take_input(Node, Solution):
    """Reads input file and returns the distance matrix."""
    filename = f'Test/Node{Node}_Solution{Solution}.txt'
    coordinates = read_tsp_coordinates(filename)
    return create_distance_matrix(coordinates)