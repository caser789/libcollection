def search(haystack, needle):
    """
    >>> search("ll", "hello")
    -1
    >>> search("", "")
    0
    >>> search("hello", "ll")
    2
    >>> search("aaaaabba", "bba")
    5
    >>> search("bbaaaaaa", "bba")
    0
    >>> search("aaaaa", "bba")
    -1
    """
    m = len(haystack)
    n = len(needle)
    if m < n:
        return -1

    if m == n == 0:
        return 0

    for i in range(m-n+1):
        j = 0
        done = False
        while not done and j < n:
            if needle[j] != haystack[i+j]:
                done = True
            j += 1

        if not done:
            return i

    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
