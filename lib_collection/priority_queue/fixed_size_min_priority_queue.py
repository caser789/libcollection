class FixedSizeMinPriorityQueue(object):

    def __init__(self):
        self.keys = [None] * 10
        self.n = 0

    @property
    def min(self):
        pass

    def pop(self):
        pass

    def insert(self, i):
        self.n += 1
        self.keys[self.n] = i
        self._swim(self.n)

    def _swim(self, n):
        """
        >>> q = FixedSizeMinPriorityQueue()
        >>> q.keys = [None, 2, 3, None, 1]
        >>> q.n = 4
        >>> q._swim(4)
        >>> q.keys
        [None, 1, 2, None, 3]
        """
        keys = self.keys
        while n > 1 and keys[n/2] > keys[n]:
            keys[n/2], keys[n] = keys[n], keys[n/2]
            n /= 2
