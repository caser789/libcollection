class UnionFind(object):

    def __init__(self, n):
        self.n = n
        self.parents = range(n)
        self.ranks = [0] * n

    def find(self, p):
        """
        >>> uf = UnionFind(5)
        >>> uf.parents = [0, 1, 2, 2, 3]
        >>> uf.find(4)
        2
        >>> uf.parents
        [0, 1, 2, 2, 2]
        """
        while p != self.parents[p]:
            self.parents[p] = self.parents[self.parents[p]]
            p = self.parents[p]
        return p

    def is_connected(self, p):
        pass

    def union(self, p, q):
        pass
