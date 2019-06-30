from lib_collection.kvstore.linked_list import LinkedListKVStore


class HashMap(object):

    def __init__(self):
        self.bucket_cnt = 3
        self.n = 0
        self.buckets = [LinkedListKVStore() for _ in range(self.bucket_cnt)]

    def __len__(self):
        """
        >>> d = HashMap()
        >>> d['a'] = 1
        >>> len(d)
        1
        >>> d['b'] = 2
        >>> d['a'] = 3
        >>> len(d)
        2
        """
        return self.n

    def __setitem__(self, k, v):
        """
        >>> d = HashMap()
        >>> d['a'] = 1
        """
        h = self._hash(k)
        bucket = self.buckets[h]
        if k not in bucket:
            self.n += 1
        bucket[k] = v

    def __getitem__(self, k):
        """
        >>> d = HashMap()
        >>> d['a'] = 1
        >>> d['a']
        1
        >>> d['b'] = 2
        >>> d['a'] = 3  # test update
        >>> d['a']
        3
        """
        h = self._hash(k)
        return self.buckets[h][k]

    def __contains__(self, k):
        """
        >>> d = HashMap()
        >>> d['a'] = 1
        >>> 'a' in d
        True
        >>> 'b' in d
        False
        """
        h = self._hash(k)
        return k in self.buckets[h]

    def __delitem__(self, k):
        """
        >>> d = HashMap()
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
        h = self._hash(k)
        bucket = self.buckets[h]
        if k in bucket:
            del bucket[k]
            self.n -= 1

    def __repr__(self):
        """
        >>> d = HashMap()
        >>> d['a'] = 1
        >>> d['b'] = 2
        >>> d['c'] = 3
        >>> d
        {'c': 3, 'a': 1, 'b': 2}
        """
        k_v = [
            "'{}': {}".format(k, v)
            for bucket in self.buckets
            for k, v in bucket
        ]
        return '{' + ', '.join(k_v) + '}'

    def __iter__(self):
        """
        >>> d = HashMap()
        >>> d['a'] = 1
        >>> d['b'] = 2
        >>> d['c'] = 3
        >>> for k, v in d:
        ...     print k, v
        ...
        c 3
        a 1
        b 2
        """
        for bucket in self.buckets:
            for k, v in bucket:
                yield k, v

    # private method
    def _hash(self, k):
        return sum(ord(c) for c in str(k)) % self.bucket_cnt
