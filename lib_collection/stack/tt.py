class Stack(object):

    def __init__(self, capacity=2):
        self.n = 0
        self.values = [None] * capacity
        self.capacity = capacity

    def push(self, v):
        if self.n == self.capacity:
            self._resize(self.capacity*2)

        self.values[self.n] = v
        self.n += 1

    def pop(self):
        if not self.n:
            return

        self.n -= 1
        v = self.values[self.n]
        if self.n and self.n == self.capacity//4:
            self._resize(self.capacity//2)

        return v

    def __len__(self):
        return self.n

    def _resize(self, capacity):
        values = [None] * capacity
        for i in range(self.n):
            values[i] = self.values[i]

        self.capacity = capacity
        self.values = values


if __name__ == '__main__':
    s = Stack()
    s.push(5)
    s.push(3)
    s.push(8)

    assert len(s) == 3

    assert s.pop() == 8
    assert len(s) == 2

    assert s.pop() == 3
    assert len(s) == 1

    assert s.pop() == 5
    assert len(s) == 0

    assert s.pop() is None
