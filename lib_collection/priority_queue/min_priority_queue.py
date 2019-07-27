class MinPriorityQueue(object):
    def __init__(self):
        self.keys = [None] * 4
        self.n = 0

    def __len__(self):
        return self.n

    def push(self, v):
        self.n += 1
        self.keys[self.n] = v
        self._swim(self.n)

    def pop(self):
        pass

    @property
    def min(self):
        """
        >>> q = MinPriorityQueue()
        >>> q.min
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 4, 1, 2]
        >>> q.n = 3
        >>> q.min
        4
        """
        if not self.n:
            raise IndexError('underflow')
        return self.keys[1]

    def _swim(self, n):
        """
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 2, 3, None, 1]
        >>> q.n = 4
        >>> q._swim(4)
        >>> q.keys
        [None, 1, 2, None, 3]
        >>> q = MinPriorityQueue()
        >>> q.keys = [None, 3, 2, None, 1]
        >>> q.n = 4
        >>> q._swim(4)
        >>> q.keys
        [None, 1, 3, None, 2]
        """
        keys = self.keys
        while n > 1 and keys[n/2] > keys[n]:
            keys[n/2], keys[n] = keys[n], keys[n/2]
            n /= 2
