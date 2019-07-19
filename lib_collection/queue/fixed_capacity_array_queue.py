class FixedCapacityArrayQueue(object):

    def __init__(self, lst=None, capacity=5):
        self.capacity = capacity
        self.n = 0

    def __len__(self):
        return self.n

    def __contains__(self, i):
        return False

    def __iter__(self):
        return []

    def __repr__(self):
        return ''

    def enqueue(self, i):
        pass

    def dequeue(self):
        pass

    @property
    def top(self):
        pass
