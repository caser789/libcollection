from undirected_graph import Graph


class DepthFirstSearch(object):
    def __init__(self, graph, v):
        self.marked = [False] * graph.v
        self.count = 0
        self.dfs(graph, v)

    def dfs(self, graph, v):
        self.count += 1
        self.marked[v] = True
        for e in graph.get_siblings(v):
            if not self.marked[e]:
                self.dfs(graph, e)


if __name__ == '__main__':
    g = Graph(13)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 5)
    g.add_edge(0, 6)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(7, 8)
    g.add_edge(9, 10)
    g.add_edge(9, 11)
    g.add_edge(9, 12)
    g.add_edge(11, 12)
    g.pprint()

    s = DepthFirstSearch(g, 0)
    for v in range(g.v):
        if s.marked[v]:
            print("{} ".format(v), end="")
    print("")
    if s.count != g.v:
        print("NOT CONNECTED")
    else:
        print("CONNECTED")


    s = DepthFirstSearch(g, 9)
    for v in range(g.v):
        if s.marked[v]:
            print("{} ".format(v), end="")
    print("")
    if s.count != g.v:
        print("NOT CONNECTED")
    else:
        print("CONNECTED")

