from collections import deque


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


class PathFinder(object):
    def __init__(self, graph, s):
        self.s = s
        self.marked = [False for _ in range(graph.v)]
        self.parents = [v for v in range(graph.v)]
        queue = deque([s])
        while queue:
            v = queue.popleft()
            self.marked[v] = True
            for w in graph.get_adjs(v):
                if self.marked[w]:
                    continue
                self.parents[w] = v
                queue.append(w)

    def has_path_to(self, w):
        return self.marked[w]

    def path_to(self, w):
        if not self.marked[w]:
            return
        res = []
        while w != self.s:
            res.append(w)
            w = self.parents[w]
        res.append(w)
        return res


if __name__ == '__main__':
    g = UndirectedGraph(6)
    g.add_edge(0, 5)
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(2, 4)
    g.add_edge(2, 3)
    g.add_edge(1, 2)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.pprint()

    p = PathFinder(g, 0)
    for v in range(g.v):
        print(p.path_to(v))
