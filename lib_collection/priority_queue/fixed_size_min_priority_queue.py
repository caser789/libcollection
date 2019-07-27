class FixedSizeMinPriorityQueue(object):

    def __init__(self, capacity=10):
        self.keys = [None] * capacity
        self.n = 0

    @property
    def min(self):
        pass

    def pop(self):
        pass

    def insert(self, i):
        """
        >>> q = FixedSizeMinPriorityQueue(capacity=4)
        >>> q.insert(3)
        >>> q.insert(2)
        >>> q.insert(1)
        >>> q.keys
        [None, 1, 3, 2]
        """
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
