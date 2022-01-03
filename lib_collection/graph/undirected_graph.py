class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.root = None
        self.n = 0

    def push(self, data):
        node = Node(data)
        node.next = self.root
        self.root = node
        self.n += 1

    def __len__(self):
        return self.n

    def __iter__(self):
        p = self.root
        while p:
            yield p.data
            p = p.next


class Graph(object):
    def __init__(self, v):
        self.v = v
        self.e = 0
        self.adj = [LinkedList() for _ in range(v)]

    def add_edge(self, v, w):
        self.adj[v].push(w)
        self.adj[w].push(v)
        self.e += 1

    def get_siblings(self, v):
        for e in self.adj[v]:
            yield e

    def get_degree(self, v):
        return len(self.adj[v])

    def pprint(self):
        print("{} vertices, {} edges".format(self.v, self.e))
        for i, lst in enumerate(self.adj):
            print("{}:".format(i), end="")
            for e in lst:
                print(" {}".format(e), end="")
            print("")


if __name__ == '__main__':
    g = Graph(13)
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
