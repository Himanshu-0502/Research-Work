import random as rd

def generate_random_tour(distance_matrix):
    """Generates a random tour."""
    tour = list(range(len(distance_matrix)))
    rd.shuffle(tour)
    return tour