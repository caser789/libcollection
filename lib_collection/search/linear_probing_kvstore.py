class LinearProbingKVStore(object):

    def __init__(self, capacity=4):
        self.capacity = capacity

    def __setitem__(self, k, v):
        pass


    def __getitem__(self, k):
        pass

    def __delitem__(self, k):
        pass

    def _hash(self, k):
        """
        >>> d = LinearProbingKVStore()
        >>> d._hash('a')
        1
        >>> d._hash('b')
        2
        >>> d._hash('c')
        3
        >>> d._hash('d')
        0
        """
        return sum(ord(i) for i in str(k)) % self.capacity
