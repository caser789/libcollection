class ResizingArrayQueue(object):

    def __init__(self, lst=None):
        self.n = 0
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
        return

    def dequeue(self):
        return

    @property
    def top(self):
        return

    def _resize(self, n):
        pass
