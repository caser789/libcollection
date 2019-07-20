class NoneNode(object):
    pass


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
        pass
