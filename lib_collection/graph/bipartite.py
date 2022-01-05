class Bipartite(object):
    def __init__(self, graph):
        self.is_bipartite = True
        self.color = [False for _ in range(graph.v)]
        self.marked = [False for _ in range(graph.v)]
        self.edge_to = [0 for _ in range(graph.v)]
        self.odd_length_cycle = []

        for v in range(graph.v):
            if not self.marked[v]:
                self.dfs(graph, v)

    def dfs(self, graph, v):
        self.marked[v] = True
        for w in graph.get_siblings(v):
            # short circuit if odd-length cycle found
            if self.odd_length_cycle:
                return

            # found uncolored vertex, so recur
            if not self.marked[w]:
                self.edge_to[w] = v
                self.color[w] = not self.color[v]
                self.dfs[graph, w]
            # if v-w create an odd-length cycle, find it
            elif self.color[w] == self.color[v]:
                self.is_bipartite = False
                self.odd_length_cycle.append(w)
                x = v
                while x != w:
                    self.odd_length_cycle.append(x)
                    x = self.edge_to[x]
                self.odd_length_cycle.append(w)

    def is_bipartite(self):
        return self.is_bipartite

    def get_color(self, v):
        if not self.is_bipartite:
            raise

        return self.color[v]
