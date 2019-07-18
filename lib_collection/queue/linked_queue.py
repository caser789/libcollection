from lib_collection.node import Node


class LinkedQueue(object):

    def __init__(self):
        self.n = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.n

    def __contains__(self, i):
        return False

    def __iter__(self):
        return []

    def __str__(self):
        return ''

    __repr__ = __str__

    def enqueue(self, i):
        """
        >>> q = LinkedQueue()
        >>> q.enqueue('a')
        >>> q.enqueue('b')
        """
        n = Node(i)
        if self.head is None:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = n
        self.n += 1

    def dequeue(self):
        """
        >>> q = LinkedQueue()
        >>> q.enqueue('a')
        >>> q.enqueue('b')
        >>> q.enqueue('c')
        >>> q.dequeue()
        'a'
        >>> q.dequeue()
        'b'
        >>> q.dequeue()
        'c'
        >>> q.dequeue()
        Traceback (most recent call last):
            ...
        IndexError: queue underflowed
        """
        if self.head is None:
            raise IndexError('queue underflowed')
        res = self.head.v
        self.head = self.head.next
        self.n -= 1
        return res

    @property
    def top(self):
        """
        >>> q = LinkedQueue()
        >>> q.top
        Traceback (most recent call last):
            ...
        IndexError: queue underflowed
        >>> q.enqueue('a')
        >>> q.top
        'a'
        >>> q.enqueue('b')
        >>> q.top
        'a'
        """
        if self.head is None:
            raise IndexError('queue underflowed')
        return self.head.v
