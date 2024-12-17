1.A*
import heapq

# Define the map of Romania as a graph
romania_map = {
    'Arad': {'Zerind': 75, 'Timisoara': 118, 'Sibiu': 140},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 85},
    'Giurgiu': {'Bucharest': 90},
    'Urziceni': {'Bucharest': 85, 'Vaslui': 142, 'Hirsova': 98},
    'Hirsova': {'Urziceni': 98, 'Eforie': 86},
    'Eforie': {'Hirsova': 86},
    'Vaslui': {'Urziceni': 142, 'Iasi': 92},
    'Iasi': {'Vaslui': 92, 'Neamt': 87},
    'Neamt': {'Iasi': 87}
}

# Define the heuristic function (straight-line distance to Bucharest)
heuristic = {
    'Arad': 366,
    'Zerind': 374,
    'Oradea': 380,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Rimnicu Vilcea': 193,
    'Fagaras': 176,
    'Pitesti': 100,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Hirsova': 151,
    'Eforie': 161,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234
}

# A* search algorithm
def a_star_search(graph, start, goal, heuristic):
    # Initialize open list with start node (priority queue)
    open_list = [(0, start)]
    
    # Set to keep track of visited nodes
    closed_set = set()
    
    # Initialize g_scores (actual cost to reach each node)
    g_score = {location: float('inf') for location in graph}
    g_score[start] = 0
    
    # Track the path
    came_from = {}
    
    while open_list:
        # Get the node with lowest f-score
        current_f, current_node = heapq.heappop(open_list)
        
        # If we've reached the goal, reconstruct and return the path
        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path, g_score[goal]
        
        # Skip if node already explored
        if current_node in closed_set:
            continue
        
        # Mark current node as explored
        closed_set.add(current_node)
        
        # Explore neighbors
        for neighbor, distance in graph[current_node].items():
            # Calculate tentative g-score (actual cost to current node)
            tentative_g = g_score[current_node] + distance
            
            # Update if we've found a better path
            if tentative_g < g_score[neighbor]:
                # Record the path
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g
                
                # Calculate f-score (actual cost + heuristic)
                f_score = tentative_g + heuristic[neighbor]
                
                # Add to open list
                heapq.heappush(open_list, (f_score, neighbor))
    
    # If no path is found
    return None, float('inf')

# Main function to demonstrate the algorithm
def main():
    # List of possible start and goal locations
    cities = list(romania_map.keys())
    
    print("Available cities:", cities)
    
    # Get user input for start and goal
    start_location = input("Enter start location: ")
    goal_location = input("Enter goal location: ")
    
    # Validate input
    if start_location not in cities or goal_location not in cities:
        print("Invalid city names. Please check the spelling.")
        return
    
    # Perform A* search
    path, shortest_distance = a_star_search(romania_map, start_location, goal_location, heuristic)
    
    # Print results
    if path:
        print(f"\nPath from {start_location} to {goal_location}:")
        print(" -> ".join(path))
        print(f"\nTotal distance: {shortest_distance} km")
    else:
        print(f"No path found from {start_location} to {goal_location}.")

