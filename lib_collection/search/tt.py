import random


class Node(object):
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.next = None


class LinkedListTable(object):
    def __init__(self):
        self.root = None

    def __setitem__(self, k, v):
        node = self._get(self.root, k)
        if node:
            node.v = v
            return

        self.root = self._put(self.root, k, v)

    def __getitem__(self, k):
        node = self._get(self.root, k)
        if node:
            return node.v

    def __delitem__(self, k):
        self.root = self._del(self.root, k)

    def _del(self, node, k):
        dummy = Node(None, None)
        dummy.next = node
        p = dummy
        while p.next and p.next.k != k:
            p = p.next

        if p and p.next.k == k:
            p.next = p.next.next

        return dummy.next

    def _put(self, node, k, v):
        if node is None:
            return Node(k, v)

        n = Node(k, v)
        n.next = node
        return n

    def _get(self, node, k):
        while node and node.k != k:
            node = node.next

        return node

    def __iter__(self):
        p = self.root
        while p:
            yield p.k, p.v
            p = p.next


class SeparateChainTable(object):
    def __init__(self, capacity=4):
        self.chains = [LinkedListTable() for _ in range(capacity)]
        self.capacity = capacity
        self.n = 0

    def _hash(self, key, capacity):
        R = 26
        h = 0
        for c in key:
            h = (h * R + ord(c) - ord('a') + 1) % 997
        return h % capacity

    def __setitem__(self, k, v):
        if self.n == self.capacity * 10:
            self._resize(self.capacity*2)

        i = self._hash(k, self.capacity)
        self.chains[i][k] = v
        self.n += 1

    def __getitem__(self, k):
        pass

    def __delitem__(self, k):
        pass

    def _resize(self, capacity):
        chains = [LinkedListTable() for _ in range(capacity)]
        for chain in self.chains:
            for k, v in chain:
                pass


if __name__ == '__main__':
    table = LinkedListTable()
    table['a'] = 1
    table['b'] = 2
    table['c'] = 3

    assert table['a'] == 1
    assert table['b'] == 2
    assert table['c'] == 3

    del table['a']
    assert table['a'] is None

    del table['b']
    assert table['b'] is None

    del table['c']
    assert table['c'] is None
