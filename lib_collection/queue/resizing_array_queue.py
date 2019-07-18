class ResizingArrayQueue(object):

    def __init__(self, lst=None):
        self.n = 0

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
        return

    def dequeue(self):
        return

    @property
    def top(self):
        return
