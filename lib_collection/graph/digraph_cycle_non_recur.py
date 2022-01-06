from collections import deque


class DigraphCycle(object):
    def __init__(self, graph):
        indegrees = [graph.get_indegree(v) for v in range(graph.v)]

        queue = deque([v for v, indegree in enumerate(indegrees) if indegree==0])
        while queue:
            v = queue.popleft()
            for w in graph.get_siblings(v):
                indegrees[w] -= 1
                if indegrees[w] == 0:
                    queue.append(w)

        edge_to = [0 for _ in range(graph.v)]
        root = -1
        for v in range(graph.v):
            if indegrees[v] == 0:
                continue

            root = v
            for w in graph.get_siblings(v):
                if indegrees[v] > 0:
                    edge_to[w] = v

        if root == -1:
            return

        cycle = []
        v = root
        while True:
            cycle.append(v)
            v = edge_to[v]
            if v == root:
                break
        cycle.append(v)
