from lib_collection.node import Node


class LinkedQueue(object):

    def __init__(self):
        self.n = 0
        self.head = Node(None)

    def __len__(self):
        return self.n

    def __contains__(self, i):
        """
        >>> q = LinkedQueue()
        >>> 'a' in q
        False
        >>> q.enqueue('a')
        >>> 'a' in q
        True
        """
        for j in self:
            if i == j:
                return True
        return False

    def __iter__(self):
        """
        >>> q = LinkedQueue()
        >>> q.enqueue('a')
        >>> q.enqueue('b')
        >>> q.enqueue('c')
        >>> for i in q:
        ...     print i
        ...
        a
        b
        c
        """
        n = self.head
        while n.next is not None:
            n = n.next
            yield n.v

    def __str__(self):
        """
        >>> q = LinkedQueue()
        >>> q.enqueue('a')
        >>> q.enqueue(2)
        >>> q.enqueue('c')
        >>> q
        LinkedQueue(['a', 2, 'c'])
        >>> print q
        LinkedQueue(['a', 2, 'c'])
        """
        return 'LinkedQueue([{}])'.format(', '.join(repr(i) for i in self))

    __repr__ = __str__

    def enqueue(self, i):
        """
        >>> q = LinkedQueue()
        >>> q.enqueue('a')
        >>> q.enqueue('b')
        """
        node = Node(i)
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = node
        self.n += 1

    def dequeue(self):
        """
        >>> q = LinkedQueue()
        >>> q.dequeue()
        Traceback (most recent call last):
            ...
        IndexError: dequeue from empty queue
        """
        if len(self) == 0:
            raise IndexError('dequeue from empty queue')

    @property
    def top(self):
        """
        >>> q = LinkedQueue()
        >>> q.top
        Traceback (most recent call last):
            ...
        IndexError: top from empty queue
        """
        if len(self) == 0:
            raise IndexError('top from empty queue')
