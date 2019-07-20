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
        """
        >>> d = BinarySearchKVStore()
        >>> len(d)
        0
        >>> d['a'] = 1
        >>> len(d)
        1
        """
        return self.n

    def __contains__(self, key):
        """
        >>> d = BinarySearchKVStore()
        >>> 'a' in d
        False
        >>> d['a'] = 1
        >>> d['b'] = 2
        >>> 'a' in d
        True
        """
        i = self.index(key)
        if i < len(self) and self.keys[i] == key:
            return True
        return False

    @property
    def min(self):
        """
        >>> # 1. test get min from empty raise underflow error
        >>> d = BinarySearchKVStore()
        >>> d.min
        Traceback (most recent call last):
            ...
        IndexError: underflow
        """
        if len(self) == 0:
            raise IndexError('underflow')

    @property
    def max(self):
        """
        >>> # 1. test get max from empty raise underflow error
        >>> d = BinarySearchKVStore()
        >>> d.max
        Traceback (most recent call last):
            ...
        IndexError: underflow
        """
        if len(self) == 0:
            raise IndexError('underflow')

    def __setitem__(self, key, value):
        """
        >>> # 1. test key in keys
        >>> d = BinarySearchKVStore()
        >>> d.keys = [1, 2]
        >>> d.values = ['a', 'b']
        >>> d.n = 2
        >>> d[1] = 'c'
        >>> d.values = ['c', 2]
        >>> # 2. test full and resize
        >>> d = BinarySearchKVStore()
        >>> d.keys = [1, 2]
        >>> d.values = ['a', 'b']
        >>> d.n = 2
        >>> d[3] = 'c'
        >>> d.keys
        [1, 2, 3, NoneNode()]
        >>> d.capacity
        4
        >>> # 3. test insert new key in the end
        >>> d = BinarySearchKVStore()
        >>> d.keys = [1, 2]
        >>> d.values = ['a', 'b']
        >>> d.n = 2
        >>> d[3] = 'c'
        >>> d.keys
        [1, 2, 3, NoneNode()]
        >>> d.values
        ['a', 'b', 'c', NoneNode()]
        >>> # 4. test insert new key in the middle
        >>> d = BinarySearchKVStore()
        >>> d.keys = [1, 3]
        >>> d.values = ['a', 'c']
        >>> d.n = 2
        >>> d[2] = 'b'
        >>> d.keys
        [1, 2, 3, NoneNode()]
        >>> d.values
        ['a', 'b', 'c', NoneNode()]
        >>> # 5. test insert new key in the head
        >>> d = BinarySearchKVStore()
        >>> d.keys = [2, 3]
        >>> d.values = ['b', 'c']
        >>> d.n = 2
        >>> d[1] = 'a'
        >>> d.keys
        [1, 2, 3, NoneNode()]
        >>> d.values
        ['a', 'b', 'c', NoneNode()]
        """
        i = self.index(key)

        # key already in keys
        if i < len(self) and self.keys[i] == key:
            self.values[i] = value
            return

        # keys are full
        if len(self) == self.capacity:
            self._resize(self.capacity*2)

        # make space for the new key
        for j in range(len(self), i, -1):
            self.keys[j] = self.keys[j-1]
            self.values[j] = self.values[j-1]

        # insert new key
        self.keys[i] = key
        self.values[i] = value
        self.n += 1

    def __getitem__(self, key):
        """
        >>> d = BinarySearchKVStore()
        >>> d['a'] = 1
        >>> d['b'] = 2
        >>> d['a']
        1
        >>> d['b']
        2
        >>> d['c']
        Traceback (most recent call last):
            ...
        KeyError: 'c'
        """
        i = self.index(key)
        if i < len(self) and self.keys[i] == key:
            return self.values[i]
        raise KeyError(key)

    def __delitem__(self, key):
        pass

    def del_max(self):
        pass

    def del_min(self):
        pass

    def index(self, key):
        """
        >>> d = BinarySearchKVStore()
        >>> d.n = 3
        >>> d.keys = [1, 2, 3]
        >>> d.index(2)
        1
        >>> d.index(1.5)
        1
        >>> d.index(2.5)
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
        >>> # 1. test resize up
        >>> d = BinarySearchKVStore()
        >>> d.n = 2
        >>> d.keys = [1, 2]
        >>> d.values = ['a', 'b']
        >>> d._resize(4)
        >>> d.keys
        [1, 2, NoneNode(), NoneNode()]
        >>> d.values
        ['a', 'b', NoneNode(), NoneNode()]
        >>> # 2. test resize Down
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
