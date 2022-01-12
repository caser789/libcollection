class Node(object):
    def __init__(self, v):
        self.next = None
        self.v = v


class LinkedList(object):
    def __init__(self):
        self.root = None
        self.n = 0

    def put(self, v):
        node = Node(v)
        node.next = self.root
        self.root = node
        self.n += 1

    def __len__(self):
        return self.n

    def __iter__(self):
        h = self.root
        while h:
            yield h.v
            h = h.next


class UndirectedGraph(object):
    def __init__(self, v):
        self.v = v
        self.e = 0
        self.adjs = [LinkedList() for _ in range(v)]

    def add_edge(self, v, w):
        self.adjs[v].put(w)
        self.adjs[w].put(v)
        self.e += 1

    def get_adjs(self, v):
        for e in self.adjs[v]:
            yield e

    def get_degree(self, v):
        return len(self.adjs[v])

    def pprint(self):
        print("{} vertices, {} edges".format(self.v, self.e))
        for i, adjs in enumerate(self.adjs):
            print("{}:".format(i), end="")
            for e in adjs:
                print(" {}".format(e), end="")
            print("")


class Connectivity(object):
    def __init__(self, graph, s):
        self.marked = [False for _ in range(graph.v)]
        self.count = 0
        self._dfs(graph, s)

    def _dfs(self, graph, s):
        self.marked[s] = True
        self.count += 1
        for w in graph.get_adjs(s):
            if self.marked[w]:
                continue
            self._dfs(graph, w)

    def is_connected(self, d):
        return self.marked[d]

if __name__ == '__main__':
    g = UndirectedGraph(13)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(0, 6)
    g.add_edge(0, 5)
    g.add_edge(3, 5)
    g.add_edge(3, 4)
    g.add_edge(4, 5)
    g.add_edge(4, 6)
    g.add_edge(7, 8)
    g.add_edge(9, 10)
    g.add_edge(9, 11)
    g.add_edge(9, 12)
    g.add_edge(11, 12)
    g.pprint()

    s = Connectivity(g, 0)
    for v in range(g.v):
        if s.marked[v]:
            print("{} ".format(v), end="")
    print("")
    if s.count != g.v:
        print("NOT CONNECTED")
    else:
        print("CONNECTED")


    s = Connectivity(g, 9)
    for v in range(g.v):
        if s.marked[v]:
            print("{} ".format(v), end="")
    print("")
    if s.count != g.v:
        print("NOT CONNECTED")
    else:
        print("CONNECTED")
