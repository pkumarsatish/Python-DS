# Graph ADT Implementation - using defaultdict(list)

from collections import defaultdict


class Graph:
    # Undirected Graph
    def __init__(self):
        self.Graph = defaultdict(list)

    def add_edge(self, u, v):
        self.Graph[u].append(v)
        self.Graph[v].append(u)

    def bfs(self, s):
        # Breadth first search
        n = len(self.Graph)
        visited = [False] * n
        q = [s]
        visited[s] = True

        while q:
            s = q.pop(0)
            print(s, end=" ")
            for nb in self.Graph[s]:
                if not visited[nb]:
                    q.append(nb)
                    visited[nb] = True
        print("")

    def dfs_rec(self, s, visited):
        visited[s] = True
        print(s, end=" ")

        for nb in self.Graph[s]:
            if not visited[nb]:
                self.dfs_rec(nb, visited)

    def dfs(self, s):
        # Depth first search
        n = len(self.Graph)
        visited = [False]*n

        self.dfs_rec(s, visited)
        print("")

    def print_graph(self):
        print(self.Graph)


class DGraph(Graph):
    # Directed Graph
    def add_edge(self, u, v):
        self.Graph[u].append(v)


if __name__ == "__main__":
    g = DGraph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)

    g.bfs(2)
    g.dfs(2)
    g.print_graph()
