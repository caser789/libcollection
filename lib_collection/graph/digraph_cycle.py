class DigraphCycle(object):
    def __init__(self, graph):
        self.marked = [False for _ in range(graph.v)]
        self.on_stack = [False for _ in range(graph.v)]
        self.edge_to = [0 for _ in range(graph.v)]
        self.cycle = []
        for v in range(graph.v):
            if self.cycle:
                return

            if self.marked[v]:
                continue

            self.dfs(graph, v)

    def dfs(self, graph, v):
        self.marked[v] = True
        self.on_stack[v] = True
        for w in graph.get_siblings(v):
            if self.cycle:
                return

            if not self.marked[v]:
                self.edge_to[w] = v
                self.dfs[graph, w]
            elif self.on_stack[w]:
                x = v
                while x != w:
                    self.cycle.append(x)
                    x = self.edge_to[x]
                self.cycle.append(w)
                self.cycle.append(v)
        self.on_stack[v] = False

    def has_cycle(self):
        return bool(self.cycle)
