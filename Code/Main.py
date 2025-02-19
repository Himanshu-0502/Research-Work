import time
import matplotlib.pyplot as plt
from Generate_Input import take_input
from Random_Tour import generate_random_tour
from Construct_Tour import construct_tour
from Tour_Optimization import tour_optimization

def tour_cost(tour, distance_matrix):
    """Calculates the cost of a given path."""
    return sum(distance_matrix[tour[i]][tour[(i+1)%len(tour)]] for i in range(len(tour)))

def solve(Node, Solution):
    """Solves the TSP problem for given nodes and solutions."""
    distance_matrix = take_input(Node, Solution)

    start_time = time.time()
    random_tour = generate_random_tour(distance_matrix)
    random_score = tour_cost(tour_optimization(random_tour, distance_matrix), distance_matrix)
    original_time = time.time() - start_time
    random_gap = round((random_score - Solution) / Solution * 100, 2)

    start_time = time.time()
    optimal_tour = construct_tour(distance_matrix)
    optimal_score = tour_cost(tour_optimization(optimal_tour, distance_matrix), distance_matrix)
    improved_time = time.time() - start_time
    optimal_gap = round((optimal_score - Solution) / Solution * 100, 2)

    time_gap = round((original_time - improved_time) / original_time * 100, 2)
    return random_gap, optimal_gap, time_gap

if __name__ == '__main__':
    nodes = [130, 131, 150, 237, 280, 493, 657, 724, 783, 1000]
    solutions = [6110, 564, 6528, 1019, 2579, 35002, 48912, 41910, 8806, 18659688]
    iterations = 10
    average_random_gaps, average_optimal_gaps, average_time_gaps = [], [], []

    for node, solution in zip(nodes, solutions):
        random_gaps, optimal_gaps, time_gaps = 0, 0, 0
        for i in range(iterations):
            random_gap, optimal_gap, time_gap = solve(node, solution)
            random_gaps += random_gap
            optimal_gaps += optimal_gap
            time_gaps += time_gap
        average_random_gaps.append(random_gaps / iterations)
        average_optimal_gaps.append(optimal_gaps / iterations)
        average_time_gaps.append(time_gaps / iterations)

    for node, solution, random_gap, optimal_gap, time_gap in zip(nodes, solutions, average_random_gaps, average_optimal_gaps, average_time_gaps):
        print(f'Solving {node} Node with {solution} Solution')
        print(f'Random 2-Opt Percentage Gap: {random_gap}')
        print(f'Optimal 2-Opt Percentage Gap: {optimal_gap}')
        print(f'Time Improvement Percentage: {time_gap}')
        print()

    plt.figure(figsize=(10, 6))
    plt.plot(nodes, average_random_gaps, marker='o', linestyle='-', color='b')
    plt.title('Random 2-Opt Percentage Gap vs. Number of Nodes')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Random 2-Opt Percentage Gap (%)')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(nodes, average_optimal_gaps, marker='o', linestyle='-', color='r')
    plt.title('Optimal 2-Opt Percentage Gap vs. Number of Nodes')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Optimal 2-Opt Percentage Gap (%)')
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(nodes, average_random_gaps, marker='o', linestyle='-', color='b', label='Random 2-Opt Percentage Gap')
    plt.plot(nodes, average_optimal_gaps, marker='o', linestyle='-', color='r', label='Optimal 2-Opt Percentage Gap')
    plt.title('Percentage Gap vs. Number of Nodes')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Percentage Gap (%)')
    plt.grid(True)
    plt.legend()
    plt.show()

    plt.figure(figsize=(10, 6))
    plt.plot(nodes, average_time_gaps, marker='o', linestyle='-', color='b')
    plt.title('Time Improvement Percentage vs. Number of Nodes')
    plt.xlabel('Number of Nodes')
    plt.ylabel('Time Improvement Percentage (%)')
    plt.grid(True)
    plt.show()

    print('Average Random 2-Opt Percentage Gap:', sum(average_random_gaps) / len(average_random_gaps))
    print('Average Optimal 2-Opt Percentage Gap:', sum(average_optimal_gaps) / len(average_optimal_gaps))
    print('Average Time Improvement Percentage:', sum(average_time_gaps) / len(average_time_gaps))