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

    def find(self, p):
        """
        >>> uf = QuickFindUnionFind(3)
        >>> uf.find(3)
        Traceback (most recent call last):
            ...
        IndexError: 3
        >>> uf.find(1)
        1
        >>> uf.find(2)
        2
        >>> uf.find(0)
        0
        """
        self._validate(p)
        return self.parents[p]

    def union(self):
        pass

    def is_connected(self, p, q):
        """
        >>> uf = QuickFindUnionFind(3)
        >>> uf.is_connected(0, 1)
        False
        >>> uf.parents[1] = 0
        >>> uf.is_connected(0, 1)
        True
        """
        self._validate(p)
        self._validate(1)
        return self.find(p) == self.find(q)

    def _validate(self, p):
        if not 0 <= p < self.n:
            raise IndexError(p)
