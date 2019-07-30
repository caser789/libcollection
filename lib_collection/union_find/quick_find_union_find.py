class QuickFindUnionFind(object):

    def __init__(self, cnt):
        self.n = cnt
        self.parents = range(cnt)

    def __len__(self):
        """
        >>> uf = QuickFindUnionFind(10)
        >>> len(uf)
        10
        """
        return self.n

    def find(self):
        pass

    def union(self):
        pass

    def is_connected(self, p, q):
        pass
