class Queue(object):

    def __init__(self):
        self.values = [None, None]
        self.p = 0
        self.q = 0
        self.n = 0
        self.capacity = 2

    def __len__(self):
        return self.n

    def enqueue(self, v):
        if self.n == self.capacity:
            self._resize(self.capacity*2)

        self.values[self.q] = v
        self.q = (self.q + 1) % self.capacity
        self.n += 1

    def dequeue(self):
        if not self.n:
            raise IndexError('underflow')

        v = self.values[self.p]
        self.p = (self.p + 1) % self.capacity

        self.n -= 1
        if self.n * 4 == self.capacity:
            self._resize(self.capacity/2)

        return v

    def _resize(self, capacity):
        values = [None] * capacity
        p = self.p
        for i in range(self.n):
            values[i] = self.values[p]
            p = (p+1)%self.capacity
        self.values = values
        self.p = 0
        self.q = self.n
        self.capacity = capacity
