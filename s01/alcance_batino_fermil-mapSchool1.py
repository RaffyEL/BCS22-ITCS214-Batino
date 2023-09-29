import heapq

graph = {
    "Home": [("Store A", 7), ("Store B", 14), ("Intersection", 25)],
    "Store A": [("Home", 7), ("Store B", 5)],
    "Store B": [("School", 7)],
    "School": [("Store B", 7), ("Intersection", 7)],
    "Intersection": [("School", 7)]
}

def shortest_path(graph, start, end):
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_vertices = {vertex: None for vertex in graph}

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor_vertex, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor_vertex]:
                distances[neighbor_vertex] = distance
                heapq.heappush(priority_queue, (distance, neighbor_vertex))
                previous_vertices[neighbor_vertex] = current_vertex

    shortest_path = []
    while end is not None:
        shortest_path.insert(0, end)
        end = previous_vertices[end]

    return distances, shortest_path

start = "Home"
end = input("""Where do you want to go?
[Store A, Store B, Intersection, School]
""").title()

distances, shortest_path = shortest_path(graph, start, end)

print(f"Shortest distances: {distances[end]}")
print(f"Shortest path from {start} to {end}: {shortest_path}")
