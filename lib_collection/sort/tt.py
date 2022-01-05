def sort(lst):
    n = len(lst)
    if n < 2:
        return

    _max = lst[0]
    for i in range(1, n):
        if lst[i] > _max:
            _max = lst[i]

    max_digit = 0
    while 10**max_digit <= _max:
        max_digit += 1


    tmp = lst[:]
    for i in range(max_digit):
        buckets = [[] for _ in range(10)]
        for v in tmp:
            t = v//(10**i)%10
            buckets[t].append(v)

        new_tmp = []
        for bucket in buckets:
            for v in bucket:
                new_tmp.append(v)
        tmp = new_tmp

    for i, v in enumerate(tmp):
        lst[i] = v


import random

for _ in range(20):
    lst = [random.randint(1, 100) for _ in range(20)]
    llst = sorted(lst)
    sort(lst)
    print(lst)
    assert llst == lst
