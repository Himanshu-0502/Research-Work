import time
from Generate_Input import take_input
from Random_Tour import generate_random_tour
from Construct_Tour import construct_tour
from Tour_Optimization import tour_optimization

def tour_cost(tour, distance_matrix):
    """Calculates the cost of a given path."""
    return sum(distance_matrix[tour[i]][tour[(i+1)%len(tour)]] for i in range(len(tour)))

def solve(Node, Solution):
    """Solves the TSP problem for given nodes and solutions."""
    print(f'Solving {Node} Node with {Solution} Solution')
    distance_matrix = take_input(Node, Solution)

    start_time = time.time()
    random_tour = generate_random_tour(distance_matrix)
    random_score = tour_cost(tour_optimization(random_tour, distance_matrix), distance_matrix)
    original_time = time.time() - start_time
    random_gap = round((random_score - Solution) / Solution * 100, 2)
    print(f'Random 2-Opt Algorithm: {random_score}, Random 2-Opt Percentage Gap: {random_gap}')

    start_time = time.time()
    optimal_tour = construct_tour(distance_matrix)
    optimal_score = tour_cost(tour_optimization(optimal_tour, distance_matrix), distance_matrix)
    improved_time = time.time() - start_time
    optimal_gap = round((optimal_score - Solution) / Solution * 100, 2)
    print(f'Optimal 2-Opt Algorithm: {optimal_score}, Optimal 2-Opt Percentage Gap: {optimal_gap}')

    time_gap = round((original_time - improved_time) / original_time * 100, 2)
    print(f'Time Improvement Percentage: {time_gap}\n')
    return random_gap, optimal_gap, time_gap

if __name__ == '__main__':
    nodes = [130, 131, 150, 198, 237, 280, 493, 657, 1000]
    solutions = [6110, 564, 6528, 15780, 1019, 2579, 35002, 48912, 18659688]
    random_gaps, optimal_gaps, time_gaps = [], [], []

    for node, solution in zip(nodes, solutions):
        random_gap, optimal_gap, time_gap = solve(node, solution)
        random_gaps.append(random_gap)
        optimal_gaps.append(optimal_gap)
        time_gaps.append(time_gap)

    print('Average Random 2-Opt Percentage Gap:', sum(random_gaps) / len(random_gaps))
    print('Average Optimal 2-Opt Percentage Gap:', sum(optimal_gaps) / len(optimal_gaps))
    print('Average Time Improvement Percentage:', sum(time_gaps) / len(time_gaps))