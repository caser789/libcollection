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

    # build dfa
    R = 256
    dfa = [[0 for _ in range(n)] for _ in range(R)]
    dfa[ord(needle[0])][0] = 1
    x = 0
    for j in range(n):
        for c in range(R):
            dfa[c][j] = dfa[c][x]
        dfa[ord(needle[j])][j] = j+1
        x = dfa[ord(needle[j])][x]

    # search
    i = j = 0
    while i < m and j < n:
        j = dfa[ord(haystack[i])][j]
        i += 1

    if j == n:
        return i - n

    return -1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
