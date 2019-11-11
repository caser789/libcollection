class FenwickTree(object):
    """
    * point update
    * range sum query

    ## last set bit
    """

    def __init__(self, n):
        self.nums = [0] * (n+1)

    def __len__(self):
        return len(self.nums) - 1

    def sum(self, i):
        assert i > 0
        s = 0
        while i > 0:
            s += self.nums[i]
            i -= i & (-i)
        return s

    def rsq(self, a, b):
        assert b >= a and a > 0 and b > 0
        return self.sum(b) - self.sum(a-1)

    def update(self, i, val):
        assert i > 0
        while i < len(self.nums):
            self.nums[i] += val
            i += i & (-i)
