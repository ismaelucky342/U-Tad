import heapq

class Graph:
    def __init__(self, directed=True):
        self.adjacency_list = {}
        self.directed = directed

    def add_edge(self, u, v, weight):
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))
        if not self.directed:
            if v not in self.adjacency_list:
                self.adjacency_list[v] = []
            self.adjacency_list[v].append((u, weight))

    def dijkstra(self, start, end):
        # Priority queue to store (distance, node)
        pq = [(0, start)]
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start] = 0
        previous_nodes = {node: None for node in self.adjacency_list}

        while pq:
            current_distance, current_node = heapq.heappop(pq)

            # If we reach the target node, stop
            if current_node == end:
                break

            # Skip if the distance is not optimal
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.adjacency_list.get(current_node, []):
                distance = current_distance + weight

                # If a shorter path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(pq, (distance, neighbor))

        # Reconstruct the shortest path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()

        return path, distances[end]

    def display_shortest_path(self, start, end):
        path, distance = self.dijkstra(start, end)
        if distance == float('inf'):
            print(f"No path exists between {start} and {end}.")
        else:
            print(f"Shortest path from {start} to {end}: {' -> '.join(map(str, path))}")
            print(f"Minimum distance: {distance}")


# Example usage
if __name__ == "__main__":
    graph = Graph(directed=False)
    graph.add_edge('A', 'B', 1)
    graph.add_edge('A', 'C', 4)
    graph.add_edge('B', 'C', 2)
    graph.add_edge('B', 'D', 6)
    graph.add_edge('C', 'D', 3)

    graph.display_shortest_path('A', 'D')