import heapq
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def add_edge(self, u, v, weight):
        self.graph[u].append((weight, v))
        self.graph[v].append((weight, u))  # Undirected graph

    def prim_mst(self):
        visited = [False] * self.V
        min_heap = [(0, 0)]  # (weight, vertex)
        mst_cost = 0
        mst_edges = []

        while min_heap:
            weight, u = heapq.heappop(min_heap)
            if visited[u]:
                continue

            visited[u] = True
            mst_cost += weight

            for w, v in self.graph[u]:
                if not visited[v]:
                    heapq.heappush(min_heap, (w, v))

            if weight != 0:
                mst_edges.append((u, weight))

        print("\nMinimum Spanning Tree Edges (with weights):")
        for edge in mst_edges:
            print(f"Node: {edge[0]} - Weight: {edge[1]}")
        print(f"Total cost of MST: {mst_cost}")


# Taking user input
def main():
    vertices = int(input("Enter the number of vertices: "))
    edges = int(input("Enter the number of edges: "))

    g = Graph(vertices)

    print("\nEnter each edge in the format: u v weight")
    for _ in range(edges):
        u, v, w = map(int, input().split())
        g.add_edge(u, v, w)

    g.prim_mst()

if __name__ == "__main__":
    main()
