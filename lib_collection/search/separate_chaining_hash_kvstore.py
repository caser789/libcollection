from lib_collection.search.sequential_search_kvstore import SequentialSearchKVStore


class SeparateChainingHashKVStore(object):

    __item_cnt_per_bucket__ = 10

    def __init__(self, bucket_cnt=4):
        self.n = 0
        self.bucket_cnt = bucket_cnt
        self.lst = [SequentialSearchKVStore() for _ in range(self.bucket_cnt)]

    def __len__(self):
        return self.n

    def __iter__(self):
        for kvstore in self.lst:
            for k in kvstore:
                yield k

    def items(self):
        for kvstore in self.lst:
            for k, v in kvstore.items():
                yield k, v

    def _hash(self, k):
        """
        >>> d = SeparateChainingHashKVStore()
        >>> d._hash('a')
        1
        >>> d._hash('b')
        2
        >>> d._hash('c')
        3
        >>> d._hash('d')
        0
        """
        return sum(ord(i) for i in str(k)) % self.bucket_cnt

    def _resize(self, bucket_cnt):
        s = SeparateChainingHashKVStore(bucket_cnt=bucket_cnt)
        for k, v in self.items():
            s[k] = v
        self.bucket_cnt = bucket_cnt
