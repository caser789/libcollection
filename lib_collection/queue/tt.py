class Queue(object):
    def __init__(self, capacity=2):
        self.capacity = capacity
        self.values = [None] * capacity
        self.n = 0
        self.head = 0
        self.tail = 0

    def enqueue(self, v):
        if self.n == self.capacity:
            self._resize(self.capacity*2)

        self.values[self.head] = v
        self.head = (self.head+1) % self.capacity
        self.n += 1

    def dequeue(self):
        if not self.n:
            return

        v = self.values[self.tail]
        self.tail = (self.tail+1) % self.capacity
        self.n -= 1

        if self.n and  self.n == self.capacity//4:
            self._resize(self.capacity//2)

        return v

    def __len__(self):
        return self.n

    def _resize(self, capacity):
        values = [None] * capacity
        t = self.tail
        for i in range(self.n):
            values[i] = self.values[t]
            t = (t+1) % self.capacity

        self.values = values
        self.capacity = capacity
        self.tail = 0
        self.head = self.n


if __name__ == '__main__':
    q = Queue()
    q.enqueue(3)
    q.enqueue(9)
    q.enqueue(6)
    q.enqueue(7)

    assert len(q) == 4

    assert q.dequeue() == 3
    assert len(q) == 3

    assert q.dequeue() == 9
    assert len(q) == 2

    assert q.dequeue() == 6
    assert len(q) == 1

    assert q.dequeue() == 7
    assert len(q) == 0

    assert q.dequeue() is None
    assert len(q) == 0
