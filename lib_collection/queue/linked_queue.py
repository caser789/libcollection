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
        pass

    def dequeue(self):
        pass

    @property
    def top(self):
        pass
