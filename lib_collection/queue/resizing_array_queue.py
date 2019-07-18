class ResizingArrayQueue(object):

    def __init__(self, lst=None, capacity=2):
        self.capacity = capacity
        self.lst = [None] * self.capacity
        self.head = 0
        self.tail = 0

    def __len__(self):
        """
        >>> queue = ResizingArrayQueue()
        >>> len(queue)
        0
        >>> queue.enqueue('a')
        >>> len(queue)
        1
        >>> queue.enqueue('b')
        >>> len(queue)
        2
        """
        res = self.tail - self.head
        if res < 0:
            res += self.capacity
        return res

    def __contains__(self, i):
        return False

    def __iter__(self):
        pass

    def __repr__(self):
        return ''

    def enqueue(self, i):
        """
        >>> queue = ResizingArrayQueue()
        >>> queue.enqueue('a')
        >>> queue.enqueue('b')
        """
        if len(self) == self.capacity:
            self._resize(self.capacity*2)

        if self.tail == self.capacity:
            self.tail = 0

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

        if len(self) * 4 <= self.capacity:
            self._resize(self.capacity/2)

        if self.head == self.capacity:
            self.head = 0

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
        return
