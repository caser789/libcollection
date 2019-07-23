class LinearProbingKVStore(object):

    def __init__(self, capacity=4):
        self.capacity = capacity
        self.n = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

    def __len__(self):
        return self.n

    def __contains__(self, k):
        pass

    def __setitem__(self, k, v):
        """
        >>> # 1. test not contains
        >>> d = LinearProbingKVStore(capacity=2)
        >>> d['a'] = 1
        >>> d.keys
        [None, 'a']
        >>> # 2. test contains
        >>> d['a'] = 2
        >>> d.keys
        [None, 'a']
        >>> # 3. test resize up
        >>> d = LinearProbingKVStore(capacity=4)
        >>> d['a'] = 1
        >>> d['b'] = 1
        >>> d['c'] = 1
        >>> d.capacity
        8
        """
        if self.n * 2 >= self.capacity:
            self._resize(self.capacity*2)

        h = self._hash(k)
        while self.keys[h] is not None:
            if self.keys[h] == k:
                self.values[h] = v
                return
            h = (h+1) % self.capacity
        self.keys[h] = k
        self.values[h] = v
        self.n += 1

    def __iter__(self):
        pass

    def items(self):
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

    def _resize(self, capacity):
        self.capacity = capacity
