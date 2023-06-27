import sys
import time
from itertools import permutations

# Graph representation
graph = {
    'a': {'b': 12, 'c': 10, 'g': 12},
    'b': {'a': 12, 'c': 8, 'd': 12},
    'c': {'a': 10, 'b': 8, 'd': 11, 'e': 3, 'g': 9},
    'd': {'b': 12, 'c': 11, 'e': 11, 'f': 10},
    'e': {'c': 3, 'd': 11, 'f': 6, 'g': 7},
    'f': {'d': 10, 'e': 6, 'g': 9},
    'g': {'a': 12, 'c': 9, 'e': 7, 'f': 9}
}

def tsp(graph):
    start_time = time.time()
    nodes = list(graph.keys())
    shortest_path = sys.maxsize

    # Generate all possible permutations of nodes
    perms = permutations(nodes)

    for path in perms:
        total_dist = 0
        prev_node = path[0]

        # Calculate total distance for current path
        for node in path[1:]:
            total_dist += graph[prev_node][node]
            prev_node = node

        # Check if current path is shorter than shortest_path
        if total_dist < shortest_path:
            shortest_path = total_dist
            best_path = path

        # Print the current iteration
        print(f"Iteration: {path} - Distance: {total_dist}")

    end_time = time.time()
    computation_time = end_time - start_time

    # Print the shortest path and computation time
    print("\nShortest Path:", best_path)
    print("Total Distance:", shortest_path)
    print("Computation Time:", computation_time, "seconds")

def dijkstra(graph, start_node, end_node):
    start_time = time.time()
    distances = {node: sys.maxsize for node in graph}
    distances[start_node] = 0
    visited = set()

    while visited != set(graph):
        current_node = min((node for node in graph if node not in visited), key=lambda x: distances[x])

        for neighbor, weight in graph[current_node].items():
            if distances[current_node] + weight < distances[neighbor]:
                distances[neighbor] = distances[current_node] + weight

        visited.add(current_node)

        # Print the current iteration
        print(f"Iteration: Visited Nodes = {visited}, Distances = {distances}")

    end_time = time.time()
    computation_time = end_time - start_time

    # Print the shortest path and computation time
    shortest_path = distances[end_node]
    print("\nShortest Path:", shortest_path)
    print("Computation Time:", computation_time, "seconds")

# Main program
choice = input("Pilih algoritma (TSP/Dijkstra): ")

if choice.lower() == "tsp":
    tsp(graph)
elif choice.lower() == "dijkstra":
    start_node = input("Enter start node: ")
    end_node = input("Enter end node: ")
    dijkstra(graph, start_node, end_node)
else:
    print("Pilihan tidak valid. Pilih antara 'TSP' atau 'Dijkstra'.")
