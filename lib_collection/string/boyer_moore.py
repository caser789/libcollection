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

    # compute skip table
    R = 256
    right = [-1 for _ in range(R)]
    for i in range(n):
        right[ord(needle[i])] = i

    # search
    i = 0
    while i <= m - n:
        skip = 0
        for j in range(n-1, -1, -1):
            if needle[j] != haystack[i+j]:
                skip = j - right[ord(haystack[i+j])]
                if skip < 1:
                    skip = 1
                break

        if skip == 0:
            return i

        i += skip

    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
