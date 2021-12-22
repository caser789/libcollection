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

    needle_hash = _hash(needle)
    for i in range(m-n+1):
        h = _hash(haystack[i:i+n])
        if h == needle_hash:
            return i

    return -1


def _hash(word):
    """
    >>> _hash("")
    0
    >>> _hash("a")
    1
    >>> _hash("z")
    26
    >>> _hash("aa")
    27
    >>> _hash("ab")
    28
    """
    res = 0
    for c in word:
        res = res * 26 + (ord(c) - ord('a') + 1)

    return res



if __name__ == '__main__':
    import doctest
    doctest.testmod()
