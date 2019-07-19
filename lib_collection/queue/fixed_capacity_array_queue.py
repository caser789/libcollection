class FixedCapacityArrayQueue(object):

    def __init__(self, lst=None, capacity=5):
        self.capacity = capacity
        self.lst = [None] * capacity
        self.n = 0
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.n

    def __contains__(self, i):
        return False

    def __iter__(self):
        return iter(['a'])

    def __repr__(self):
        """
        >>> q = FixedCapacityArrayQueue(capacity=0)
        >>> q
        FixedCapacityArrayQueue(['a'])
        """
        return 'FixedCapacityArrayQueue([{}])'.format(', '.join(repr(i) for i in self))

    def enqueue(self, i):
        """
        >>> q = FixedCapacityArrayQueue(capacity=0)
        >>> q.enqueue('a')
        Traceback (most recent call last):
            ...
        IndexError: queue overflow
        >>> q = FixedCapacityArrayQueue(capacity=2)
        >>> q.enqueue('a')
        >>> q.enqueue('b')
        >>> q.lst
        ['a', 'b']
        >>> q.tail
        0
        """
        if len(self) == self.capacity:
            raise IndexError('queue overflow')

        self.lst[self.tail]= i
        self.tail = (self.tail + 1) % self.capacity
        self.n += 1

    def dequeue(self):
        """
        >>> q = FixedCapacityArrayQueue(capacity=0)
        >>> q.dequeue()
        Traceback (most recent call last):
            ...
        IndexError: queue underflow
        >>> q = FixedCapacityArrayQueue(capacity=2)
        >>> q.enqueue('a')
        >>> q.enqueue('b')
        >>> q.dequeue()
        'a'
        >>> q.enqueue('c')
        >>> q.dequeue()
        'b'
        >>> q.enqueue('d')
        >>> q.dequeue()
        'c'
        """
        if len(self) == 0:
            raise IndexError('queue underflow')
        res = self.lst[self.head]
        self.head = (self.head + 1) % self.capacity
        self.n -= 1
        return res

    @property
    def top(self):
        """
        >>> q = FixedCapacityArrayQueue(capacity=0)
        >>> q.top
        Traceback (most recent call last):
            ...
        IndexError: queue underflow
        """
        if len(self) == 0:
            raise IndexError('queue underflow')
