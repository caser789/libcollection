class FixedSizeMaxPriorityQueue(object):

    def __init__(self, capacity=4):
        self.keys = [None] * capacity
        self.n = 0

    def __len__(self):
        return self.n

    def push(self, i):
        pass

    def pop(self):
        pass

    @property
    def max(self):
        """
        >>> q = FixedSizeMaxPriorityQueue()
        >>> q.max
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> q = FixedSizeMaxPriorityQueue()
        >>> q.keys = [None, 1, 2, 3]
        >>> q.n = 3
        >>> q.max
        1
        """
        if not self.n:
            raise IndexError('underflow')
        return self.keys[1]
