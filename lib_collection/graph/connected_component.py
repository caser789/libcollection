from undirected_graph import Graph


class CC(object):

    def __init__(self, graph):
        self.marked = [False for _ in range(graph.v)]
        self.ids = [0 for _ in range(graph.v)]
        self.count = 0
        for v in range(graph.v):
            if not self.marked[v]:
                self.dfs(graph, v)
                self.count += 1

    def dfs(self, graph, v):
        self.marked[v] = True
        self.ids[v] = self.count
        for w in graph.get_siblings(v):
            if not self.marked[w]:
                self.dfs(graph, w)

    def is_connected(self, v, w):
        return self.ids[v] == self.ids[w]

    def get_id(self, v):
        return self.ids[v]

    def get_count(self):
        return self.count



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
    print("")

    c = CC(g)
    print("{} componenets".format(c.get_count()))

    vs_by_id = [[] for _ in range(c.get_count())]
    for v in range(g.v):
        vs_by_id[c.get_id(v)].append(v)

    for group in vs_by_id:
        print(group)
