class FixedCapacityArrayQueue(object):

    def __init__(self, lst=None, capacity=5):
        self.capacity = capacity
        self.lst = [None] * capacity
        self.n = 0

    def __len__(self):
        return self.n

    def __contains__(self, i):
        return False

    def __iter__(self):
        return []

    def __repr__(self):
        return ''

    def enqueue(self, i):
        """
        >>> q = FixedCapacityArrayQueue(capacity=0)
        >>> q.enqueue('a')
        Traceback (most recent call last):
            ...
        IndexError: queue overflow
        """
        if len(self) == self.capacity:
            raise IndexError('queue overflow')

    def dequeue(self):
        """
        >>> q = FixedCapacityArrayQueue(capacity=0)
        >>> q.dequeue()
        Traceback (most recent call last):
            ...
        IndexError: queue underflow
        """
        if len(self) == 0:
            raise IndexError('queue underflow')

    @property
    def top(self):
        pass
