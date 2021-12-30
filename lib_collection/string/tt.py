R = 256
Q = 997


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

    text_hash = _hash(haystack, n)
    pattern_hash = _hash(needle, n)

    if text_hash == pattern_hash and check(haystack, needle, n, 0):
        return 0

    RM = R**(n-1) % Q
    for i in range(n, m):
        text_hash = (text_hash + Q - (ord(haystack[i-n]) - ord('a') + 1) * RM % Q) % Q
        text_hash = (text_hash * R + ord(haystack[i]) - ord('a') + 1) % Q
        if text_hash == pattern_hash and check(haystack, needle, n, i-n+1):
            return i-n+1

    return -1


def _hash(key, n):
    h = 0
    for i in range(n):
        h = (h * R + ord(key[i]) - ord('a') + 1) % Q
    return h


def check(a, b, n, i):
    for j in range(n):
        if a[i+j] != b[j]:
            return False
    return True


if __name__ == '__main__':
    import doctest
    doctest.testmod()
