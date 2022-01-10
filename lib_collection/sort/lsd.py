def sort(keys):
    key = keys[0]
    n = len(key)
    R = 256
    aux = keys[:]

    for i in range(n-1, -1, -1):
        counter = [0 for _ in range(R+1)]
        for j in range(len(keys)):
            c = keys[j][i]
            counter[ord(c)+1] += 1

        for j in range(1, R+1):
            counter[j] += counter[j-1]

        for j in range(len(keys)):
            c = keys[j][i]
            index = counter[ord(c)]
            aux[index] = keys[j]
            counter[ord(c)] += 1

        for j in range(len(keys)):
            keys[j] = aux[j]


if __name__ == '__main__':
    a = [
        '4PGC938',
        '2IYE230',
        '3CI0720',
        '1ICK750',
        '1OHV845',
        '4JZY524',
        '1ICK750',
        '3CI0720',
        '1OHV845',
        '1OHV845',
        '2RLA629',
        '2RLA629',
        '3ATW723',
    ]

    expected = [
        '1ICK750',
        '1ICK750',
        '1OHV845',
        '1OHV845',
        '1OHV845',
        '2IYE230',
        '2RLA629',
        '2RLA629',
        '3ATW723',
        '3CI0720',
        '3CI0720',
        '4JZY524',
        '4PGC938',
    ]

    sort(a)

    assert a == sorted(a)
