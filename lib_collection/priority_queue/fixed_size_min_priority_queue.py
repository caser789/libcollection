class FixedSizeMinPriorityQueue(object):

    def __init__(self, capacity=10):
        self.keys = [None] * capacity
        self.n = 0

    @property
    def min(self):
        """
        >>> # 1. Test underflow
        >>> q = FixedSizeMinPriorityQueue()
        >>> q.min
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> # 2. Test min
        >>> q.insert(3)
        >>> q.min
        3
        >>> q.insert(2)
        >>> q.min
        2
        >>> q.insert(1)
        >>> q.min
        1
        >>> q.insert(4)
        >>> q.min
        1
        """
        if self.n == 0:
            raise IndexError('underflow')
        return self.keys[1]

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
