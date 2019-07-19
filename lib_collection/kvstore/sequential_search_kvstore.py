class KVNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __repr__(self):
        """
        >>> d = KVNode('a', 1)
        >>> d
        KVNode('a', 1)
        """
        return 'KVNode({}, {})'.format(repr(self.key), repr(self.value))


class SequentialSearchKVStore(object):

    def __init__(self):
        self.n = 0
        self.head = None

    def __len__(self):
        """
        >>> d = SequentialSearchKVStore()
        >>> len(d)
        0
        >>> d['a'] = 1
        >>> len(d)
        1
        >>> d['b'] = 2
        >>> len(d)
        2
        >>> d['a'] = 3
        >>> len(d)
        2
        """
        return self.n

    def __contains__(self, key):
        """
        >>> d = SequentialSearchKVStore()
        >>> 'a' in d
        False
        >>> d['a'] = 1
        >>> 'a' in d
        True
        """
        return self._get_node(key) is not None

    def __getitem__(self, key):
        """
        >>> d = SequentialSearchKVStore()
        >>> d['a']
        Traceback (most recent call last):
            ...
        KeyError: 'a'
        >>> d['a'] = 1
        >>> d['a']
        1
        >>> d['a'] = 2
        >>> d['a']
        2
        """
        n = self._get_node(key)
        if n is None:
            raise KeyError(key)
        return n.value

    def __setitem__(self, key, value):
        """
        >>> d = SequentialSearchKVStore()
        >>> d['a'] = 1
        """
        n = self._get_node(key)
        if n:
            n.value = value
        else:
            node = KVNode(key, value)
            node.next = self.head
            self.head = node
            self.n += 1

    def __delitem__(self, key):
        """
        >>> d = SequentialSearchKVStore()
        >>> d['a'] = 1
        >>> 'a' in d
        True
        >>> len(d)
        1
        >>> del d['a']
        >>> 'a' in d
        False
        >>> len(d)
        0
        """
        self.head = self._delete_node(self.head, key)

    def __iter__(self):
        pass

    def __repr__(self):
        return ''

    def _get_node(self, key):
        n = self.head
        for _ in range(len(self)):
            if n.key == key:
                return n
            n = n.next

    def _delete_node(self, node, key):
        if node is None:
            return
        if node.key == key:
            self.n -= 1
            return node.next
        node.next = self._delete_node(node.next, key)
        return node
