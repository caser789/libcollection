from lib_collection.node import Node


class LinkedQueue(object):

    def __init__(self):
        self.n = 0
        self.head = Node(None)

    def __len__(self):
        return self.n

    def __contains__(self, i):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        return ''

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
