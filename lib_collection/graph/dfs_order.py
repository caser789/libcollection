class DFSOrder(object):
    def __init__(self, graph):
        self.marked = [False for _ in range(graph.v)]
        self.pre = [0 for _ in range(graph.v)]
        self.post = [0 for _ in range(graph.v)]
        self.pre_order = []
        self.post_order = []
        self.pre_counter = 0
        self.post_counter = 0

        for v in range(graph.v):
            if not self.marked[v]:
                self.dfs(graph, v)

    def dfs(self, graph, v):
        self.marked[v] = True
        self.pre[v] = self.pre_counter
        self.pre_counter += 1
        self.pre_order.append(v)

        for w in graph.get_siblings(v):
            if not self.marked[w]:
                self.dfs(graph, w)

        self.post[v] = self.post_counter
        self.post_counter += 1
        self.post_order.append(v)


if __name__ == '__main__':
    from digraph import Digraph
    d = Digraph(13)
    d.add_edge(0, 6)
    d.add_edge(0, 1)
    d.add_edge(0, 5)
    d.add_edge(2, 0)
    d.add_edge(2, 3)
    d.add_edge(3, 5)
    d.add_edge(5, 4)
    d.add_edge(6, 4)
    d.add_edge(6, 9)
    d.add_edge(7, 6)
    d.add_edge(8, 7)
    d.add_edge(9, 10)
    d.add_edge(9, 11)
    d.add_edge(9, 12)
    d.add_edge(11, 12)
    d.pprint()

    order = DFSOrder(d)
    print(order.pre)
    print(order.post)
    print(order.pre_order)
    print(order.post_order)
