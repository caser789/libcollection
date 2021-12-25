Q = 997
R = 26

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

    pattern_hash = _hash(needle, n)
    text_hash = _hash(haystack, n)

    if pattern_hash == text_hash and check(haystack, needle, 0):
        return 0

    index = R**(n-1) % Q

    for i in range(n, m):
        text_hash = (text_hash + Q - (ord(haystack[i-n]) - ord('a') + 1) * index % Q) % Q
        text_hash = (text_hash * R + ord(haystack[i]) - ord('a') + 1) % Q
        if text_hash == pattern_hash and check(haystack, needle, i-n+1):
            return i - n+1

    return -1


def check(text, pattern, i):
    """
    >>> check('a', 'a', 0)
    True
    >>> check('a', 'b', 0)
    False
    >>> check('aba', 'ba', 1)
    True
    >>> check('abb', 'ba', 1)
    False
    """
    for j in range(len(pattern)):
        if text[i+j] != pattern[j]:
            return False

    return True

def _hash(key, n):
    """
    >>> _hash('', 0)
    0
    >>> _hash('a', 1)
    1
    >>> _hash('ab', 2)
    28
    """
    h = 0
    for i in range(n):
        h = (h*R + ord(key[i]) - ord('a') + 1) % Q
    return h

if __name__ == '__main__':
    import doctest
    doctest.testmod()
