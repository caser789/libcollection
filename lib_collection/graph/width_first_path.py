from undirected_graph import Graph
from collections import deque


class WidthFirstPaths(object):
    def __init__(self, graph, s):
        self.marked = [False] * graph.v
        self.edge_to = [0 for i in range(graph.v)]
        self.dist_to = [float('inf') for i in range(graph.v)]
        self.s = s

        q = deque([s])
        self.marked[s] = True
        self.edge_to[s] = s
        self.dist_to[s] = 0
        while q:
            v = q.popleft()
            for w in graph.get_siblings(v):
                if not self.marked[w]:
                    print("-{}->{}".format(w, v))
                    self.marked[w] = True
                    self.edge_to[w] = v
                    self.dist_to[w] = self.dist_to[v] + 1
                    print(self.edge_to)
                    q.append(w)

    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return

        stack = []
        while v != self.s:
            stack.append(v)
            v = self.edge_to[v]
        stack.append(self.s)
        return stack


if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(0, 5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.pprint()

    p = WidthFirstPaths(g, 0)
    for v in range(g.v):
        print(p.path_to(v))
