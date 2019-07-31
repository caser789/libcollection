class QuickUnionUnionFind(object):

    def __init__(self, n):
        self.n = n
        self.parents = range(n)

    def union(self, p, q):
        pass

    def find(self, p):
        """
        >>> uf = QuickUnionUnionFind(3)
        >>> uf.find(1)
        1
        >>> uf = QuickUnionUnionFind(5)
        >>> uf.parents = [0, 1, 1, 2, 4]
        >>> uf.find(3)
        1
        """
        while p != self.parents[p]:
            p = self.parents[p]
        return p

    def is_connected(self, p, q):
        """
        >>> uf = QuickUnionUnionFind(5)
        >>> uf.parents = [0, 1, 1, 2, 4]
        >>> uf.is_connected(1, 3)
        True
        >>> uf.is_connected(1, 4)
        False
        """
        return self.find(p) == self.find(q)
