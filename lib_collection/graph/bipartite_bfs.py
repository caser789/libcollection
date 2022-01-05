from collections import deque
WHITE = False
BLACK = True


class Bipartite(object):
    def __init__(self, graph):
        self.is_bipartite = True
        self.marked = [False for _ in range(graph.v)]
        self.color = [WHITE for _ in range(graph.v)]
        self.edge_to = [0 for _ in range(graph.v)]
        self.cycle = []

        for v in range(graph.v):
            if not self.is_bipartite:
                break
            if not self.marked[v]:
                self.bfs(graph, v)

    def bfs(self, graph, s):
        self.marked[s] = True
        self.color[s] = WHITE
        q = deque([s])
        while q:
            v = q.popleft()
            for w in graph.get_siblings(v):
                if not self.marked[w]:
                    self.marked[w] = True
                    self.edge_to[w] = v
                    self.color[w] = not self.color[v]
                    q.append(w)
                elif self.color[w] == self.color[v]:
                    self.is_bipartite = False
                    x = v
                    y = w
                    stack = []
                    while x != y:
                        stack.append(x)
                        self.cycle.append(y)
                        x = self.edge_to[x]
                        y = self.edge_to[y]
                    stack.append(x)
                    while stack:
                        self.cycle.append(stack.pop())
                    self.cycle.append(w)


    def is_bipartite(self):
        return self.is_bipartite
