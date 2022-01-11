R = 256

def sort(keys):
    n = len(keys)
    aux = keys[:]
    _sort(keys, 0, n-1, 0, aux)


def get_r(key, i):
    n = len(key)
    if i < n:
        return ord(key[i])
    return -1


def _sort(keys, lo, hi, index, aux):
    if hi <= lo:
        return

    counter = [0 for _ in range(R+2)]
    for i in range(lo, hi+1):
        r = get_r(keys[i], index)
        counter[r+2] += 1

    for i in range(1, R+2):
        counter[i] += counter[i-1]

    for i in range(lo, hi+1):
        r = get_r(keys[i], index)
        j = counter[r+1]
        aux[j] = keys[i]
        counter[r+1] += 1

    for i in range(lo, hi+1):
        keys[i] = aux[i-lo]

    for i in range(R):
        _sort(keys, lo+counter[i], lo+counter[i+1]-1, index+1, aux)


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

    expected = [
        'are',
        'by',
        'seashells',
        'seashells',
        'seashore',
        'sells',
        'sells',
        'she',
        'she',
        'shells',
        'surely',
        'the',
        'the',
    ]

    print(keys)
    sort(keys)
    print("")
    print(keys)
