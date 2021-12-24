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

    i = j = 0
    while i < m and j < n:
        if haystack[i] == needle[j]:
            j += 1
        else:
            i -= j
            j = 0

        if j == n:
            return i-j+1

        i += 1

    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
