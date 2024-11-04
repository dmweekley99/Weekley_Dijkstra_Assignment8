import heapq

def dijkstra(graph, start_vertex):
    """
    Implements Dijkstra's algorithm to find the shortest paths from a start vertex to all other vertices in a graph.

    Parameters:
    graph (dict): A dictionary representing the graph where keys are vertices and values are dictionaries of neighboring vertices and edge weights.
    start_vertex (str): The vertex from which to calculate shortest paths.

    Returns:
    tuple: A tuple containing two dictionaries:
        - dist: The shortest distance from the start vertex to each vertex.
        - prev: The previous vertex on the shortest path for each vertex.
    """
    
    # Initialize distances with infinity for all vertices, and previous vertices as None
    dist = {vertex: float('infinity') for vertex in graph}
    prev = {vertex: None for vertex in graph}
    
    # Set the distance for the start vertex to zero
    dist[start_vertex] = 0

    # Create a priority queue to store vertices to explore, starting with the start vertex
    priority_queue = [(0, start_vertex)]  # (distance, vertex)

    while priority_queue:
        # Get the vertex with the smallest distance from the priority queue
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # If the distance is greater than the recorded distance, skip processing
        if current_distance > dist[current_vertex]:
            continue

        # Explore the neighbors of the current vertex
        for neighbor, weight in graph[current_vertex].items():
            # Calculate the distance to the neighboring vertex
            distance = current_distance + weight

            # If the calculated distance is less than the recorded distance, update it
            if distance < dist[neighbor]:
                dist[neighbor] = distance
                prev[neighbor] = current_vertex  # Update the previous vertex
                # Add the neighbor to the priority queue for exploration
                heapq.heappush(priority_queue, (distance, neighbor))

    return dist, prev

# Graph representation
graph = {
    'a': {'b': 4, 'c': 3},   # Vertex 'a' connected to 'b' with weight 4 and 'c' with weight 3
    'b': {'a': 4, 'e': 12, 'f': 5},  # Vertex 'b' connected to 'a', 'e', and 'f'
    'c': {'a': 3, 'd': 7},   # Vertex 'c' connected to 'a' and 'd'
    'd': {'c': 7, 'e': 2},   # Vertex 'd' connected to 'c' and 'e'
    'e': {'c': 10, 'd': 2, 'b': 12, 'z': 5},  # Vertex 'e' connected to multiple vertices
    'f': {'b': 5, 'z': 16},  # Vertex 'f' connected to 'b' and 'z'
    'z': {'f': 16, 'e': 5},  # Vertex 'z' connected to 'f' and 'e'
}

# Prompt the user to choose a starting vertex
start_vertex = input("Choose vertex (a, b, c, d, e, f, or z) to find shortest path from start vertex to other vertices: ")
distances, previous_vertices = dijkstra(graph, start_vertex)

# Output the results showing distances and previous vertices for path reconstruction
print("Distances from start vertex:", distances)
print("Previous vertices on shortest paths:", previous_vertices)
