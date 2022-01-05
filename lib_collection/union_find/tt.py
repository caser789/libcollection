class UF(object):
    def __init__(self, n):
        self.parents = [i for i in range(n)]
        self.weights = [1 for i in range(n)]
        self.n = n

    def find(self, i):
        while i != self.parents[i]:
            self.parents[i] = self.parents[self.parents[i]]
            i = self.parents[i]
        return i

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return

        if self.weights[i] < self.weights[j]:
            self.parents[i] = j
            self.weights[j] += self.weights[i]
        else:
            self.parents[j] = i
            self.weights[i] += self.weights[j]

        self.n -= 1

    def is_connected(self, p, q):
        i = self.find(p)
        j = self.find(q)
        return i== j

    def __len__(self):
        return self.n


if __name__ == '__main__':
    uf = UF(10)
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(2, 4)

    assert len(uf) == 7

    assert uf.is_connected(1, 4)
    assert not uf.is_connected(1, 5)
