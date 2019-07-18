class ResizingArrayQueue(object):

    def __init__(self, lst=None):
        self.capacity = 2
        self.lst = [None] * self.capacity
        self.head = 0
        self.tail = 0

    def __len__(self):
        return self.tail - self.head

    def __contains__(self, i):
        return False

    def __iter__(self):
        return []

    def __repr__(self):
        return ''

    def enqueue(self, i):
        """
        >>> queue = ResizingArrayQueue()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        """
        self.lst[self.tail] = i
        self.tail += 1

    def dequeue(self):
        """
        >>> queue = ResizingArrayQueue()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        >>> queue.dequeue()
        'a'
        >>> queue.dequeue()
        'b'
        >>> queue.dequeue()
        Traceback (most recent call last):
            ...
        IndexError: dequeue from empty queue
        """
        if self.head == self.tail:
            raise IndexError('dequeue from empty queue')
        res = self.lst[self.head]
        self.head += 1
        return res

    @property
    def top(self):
        """
        >>> queue = ResizingArrayQueue()
        >>> queue.top
        Traceback (most recent call last):
            ...
        IndexError: top from empty queue
        """
        if self.head == self.tail:
            raise IndexError('top from empty queue')

    def _resize(self, n):
        pass
