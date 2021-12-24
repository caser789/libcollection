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

    # build nxt
    nxt = [0 for _ in range(n+1)]
    nxt[0] = -1
    i = 1
    j = -1
    while i < n:
        if j == -1 or needle[i] == needle[j]:
            i += 1
            j += 1
            nxt[i] = j
        else:
            j = nxt[j]

    # search
    i = j = 0
    while i < m and j < n:
        if j == -1 or haystack[i] == needle[j]:
            i += 1
            j += 1
        else:
            j = nxt[j]
    if j == n:
        return i - j

    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
