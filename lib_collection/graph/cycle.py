class Cycle(object):
    def __init__(self, graph):
        self.cycle = None
        if self.has_parallel_edges(graph):
            return

        self.marked = [False for _ in range(graph.v)]
        self.edge_to = [0 for _ in range(graph.v)]
        for v in range(graph.v):
            if not self.marked[v]:
                self.dfs(graph, -1, v)

    def dfs(self, graph, u, v):
        self.marked[v] = True
        for w in graph.get_siblings(v):
            if self.cycle:
                return

            if not self.marked[w]:
                self.edge_to[w] = v
                self.dfs(graph, v, w)
            elif w != u:
                # check for cycle (but disregard reverse of edge leading to v)
                x = v
                stack = []
                while x != w:
                    stack.append(x)
                    x = self.edge_to[x]
                stack.append(w)
                stack.append(v)
                self.stack = stack

    def has_self_loop(self, graph):
        for v in range(graph.v):
            for w in graph.get_siblings(v):
                if v == w:
                    self.cycle = [v, v]
                    return True
        return False

    def has_parallel_edges(self, graph):
        marked = [False for _ in range(graph.v)]
        for v in range(graph.v):
            for w in graph.get_siblings(v):
                if marked[w]:
                    self.cycle = [v, w, v]
                    return True
                marked[w] = True

            for w in graph.get_siblings(v):
                marked[w] = False

        return False

    def has_cycle(self):
        return bool(self.cycle)
