class Queue(object):
    def __init__(self, capacity=2):
        self.values = [None] * capacity
        self.n = 1
        self.capacity = capacity

    def __len__(self):
        return self.n-1

    def _resize(self, capacity):
        values = [None] * capacity
        for i in range(self.n):
            values[i] = self.values[i]

        self.values = values
        self.capacity = capacity

    def _swim(self, n):
        while n > 1:
            h = n//2
            if self.values[h] > self.values[n]:
                break
            self.values[h], self.values[n] = self.values[n], self.values[h]
            n = h

    def _sink(self, n):
        h = 1
        while h*2 <= n:
            j = h*2
            if j+1 <= n and self.values[j+1] > self.values[j]:
                j += 1

            if self.values[h] > self.values[j]:
                break

            self.values[h], self.values[j] = self.values[j], self.values[h]
            h = j

    def enqueue(self, v):
        if self.n == self.capacity:
            self._resize(self.capacity*2)

        self.values[self.n] = v
        self._swim(self.n)
        self.n += 1

    def dequeue(self):
        if len(self) == 0:
            return

        v = self.values[1]
        self.n -= 1
        self.values[1], self.values[self.n] = self.values[self.n], self.values[1]
        self._sink(self.n-1)

        if self.n-1 == self.capacity//4:
            self._resize(self.capacity//2)

        return v

    def max(self):
        if len(self) == 0:
            return

        return self.values[1]


if __name__ == '__main__':
    q = Queue()
    q.enqueue(2)
    q.enqueue(9)
    q.enqueue(3)
    q.enqueue(8)
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(0)
    q.enqueue(1)
    q.enqueue(4)
    q.enqueue(6)

    for i in range(len(q)):
        assert q.max() == 9-i
        assert q.dequeue() == 9-i
