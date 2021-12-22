def find(haystack, needle):
    """
    >>> find("ll", "hello")
    -1
    >>> find("", "")
    0
    >>> find("hello", "ll")
    2
    >>> find("aaaaabba", "bba")
    5
    >>> find("bbaaaaaa", "bba")
    0
    >>> find("aaaaa", "bba")
    -1
    """
    m = len(haystack)
    n = len(needle)
    if m < n:
        return -1

    if m == n == 0:
        return 0

    indexes = [26**i for i in range(n)]  # [1, 26, 26*26]

    needle_hash = 0
    for i, c in enumerate(needle):
        s = _hash(c)
        needle_hash += s * indexes[i]

    haystack_hash = 0
    for i in range(n):
        c = haystack[i]
        s = _hash(c)
        haystack_hash += s * indexes[i]

    if haystack_hash == needle_hash:
        return 0

    j = 0
    for i in range(n, m):
        p = _hash(haystack[j])
        q = _hash(haystack[i])
        haystack_hash = (haystack_hash - p) / 26 + q * indexes[-1]
        if haystack_hash == needle_hash:
            return j+1
        j += 1

    return -1


def _hash(c):
    return ord(c) - ord('a') + 1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
