class NoneNode(object):
    def __repr__(self):
        return 'NoneNode()'


none = NoneNode()

class BinarySearchKVStore(object):

    def __init__(self, capacity=2):
        self.n = 0
        self.keys = [none] * capacity
        self.values = [none] * capacity
        self.capacity = capacity

    def __len__(self):
        return self.n

    def __contains__(self, key):
        return False

    @property
    def min(self):
        pass

    @property
    def max(self):
        pass

    def __setitem__(self, key, value):
        i = self.get_index(key)

        # key already in keys
        if i < len(self) and self.keys[i] == key:
            self.values[i] = value
            return

        # keys are full
        if len(self) == self.capacity:
            self._resize(self.capacity*2)

    def __getitem__(self, key):
        pass

    def __delitem__(self, key):
        pass

    def del_max(self):
        pass

    def del_min(self):
        pass

    def get_index(self, key):
        """
        >>> d = BinarySearchKVStore()
        >>> d.n = 3
        >>> d.keys = [1, 2, 3]
        >>> d.get_index(2)
        1
        >>> d.get_index(1.5)
        1
        >>> d.get_index(2.5)
        2
        """
        lo = 0
        hi = self.n - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if key == self.keys[mid]:
                return mid
            elif key < self.keys[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def _resize(self, capacity):
        """
        # test resize up
        >>> d = BinarySearchKVStore()
        >>> d.n = 2
        >>> d.keys = [1, 2]
        >>> d.values = ['a', 'b']
        >>> d._resize(4)
        >>> d.keys
        [1, 2, NoneNode(), NoneNode()]
        >>> d.values
        ['a', 'b', NoneNode(), NoneNode()]
        >>> # test resize Down
        >>> d = BinarySearchKVStore()
        >>> d.n = 2
        >>> d.keys = [1, 2, NoneNode(), NoneNode(), NoneNode(), NoneNode(), NoneNode(), NoneNode()]
        >>> d.values = ['a', 'b', NoneNode(), NoneNode(), NoneNode(), NoneNode(), NoneNode(), NoneNode()]
        >>> d._resize(2)
        >>> d.keys
        [1, 2]
        >>> d.values
        ['a', 'b']
        """
        keys = [none] * capacity
        values = [none] * capacity
        for i in range(len(self)):
            keys[i] = self.keys[i]
            values[i] = self.values[i]

        self.keys = keys
        self.values = values
        self.capacity = capacity
