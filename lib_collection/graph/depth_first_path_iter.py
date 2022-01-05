from undirected_graph import Graph


class DepthFirstPaths(object):
    def __init__(self, graph, s):
        self.marked = [False] * graph.v
        self.parent = [0 for i in range(graph.v)]
        self.s = s
        stack = [s]
        self.marked[s] = True
        while stack:
            w = stack.pop()
            for e in list(graph.get_siblings(w))[::-1]:
                if not self.marked[e]:
                    self.marked[e] = True
                    self.parent[e] = w
                    stack.append(e)


    def has_path_to(self, v):
        return self.marked[v]

    def path_to(self, v):
        if not self.has_path_to(v):
            return

        stack = []
        while v != self.s:
            stack.append(v)
            v = self.parent[v]
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

    p = DepthFirstPaths(g, 0)
    for v in range(g.v):
        print(p.path_to(v))
