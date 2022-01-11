def sort(keys):
    _sort(keys, 0, len(keys)-1, 0)


def _sort(keys, lo, hi, start):
    if hi <= lo:
        return

    lt = lo
    gt = hi
    v = get_r(keys[lt], start)
    i = lt + 1
    while i <= gt:
        c = get_r(keys[i], start)
        if c < v:
            keys[lt], keys[i] = keys[i], keys[lt]
            lt += 1
            i += 1
        elif c > v:
            keys[i], keys[gt] = keys[gt], keys[i]
            gt -= 1
        else:
            i += 1

    _sort(keys, lo, lt-1, start)
    if v >= 0:
        _sort(keys, lt, gt, start+1)
    _sort(keys, gt+1, hi, start)


def get_r(key, i):
    if i < len(key):
        return ord(key[i])

    return -1


if __name__ == '__main__':
    keys = [
        'she',
        'sells',
        'seashells',
        'by',
        'the',
        'seashore',
        'the',
        'shells',
        'she',
        'sells',
        'are',
        'surely',
        'seashells',
    ]

    expected = sorted(keys[:])
    assert keys != expected

    sort(keys)
    assert keys == expected


