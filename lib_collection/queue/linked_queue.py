from lib_collection.node import Node


class LinkedQueue(object):

    def __init__(self):
        self.n = 0

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
        pass

    def dequeue(self):
        pass

    @property
    def top(self):
        """
        >>> q = LinkedQueue()
        >>> q.top
        Traceback (most recent call last):
            ...
        IndexError: pop from empty queue
        """
        if len(self) == 0:
            raise IndexError('pop from empty queue')
