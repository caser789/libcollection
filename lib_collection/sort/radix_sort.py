def sort(lst):
    digit = 0
    max_digit = 1
    max_value = max(lst)
    while 10**max_digit <= max_value:
        max_digit += 1

    cols = lst[:]
    while digit < max_digit:
        buckets = [[] for _ in range(10)]
        for v in cols:
            t = (v//(10**digit))%10
            buckets[t].append(v)

        tmp = []
        for bucket in buckets:
            for v in bucket:
                tmp.append(v)

        cols = tmp
        digit += 1

    for i, v in enumerate(cols):
        lst[i] = v


import random

for _ in range(20):
    lst = [random.randint(1, 100) for _ in range(20)]
    llst = sorted(lst)
    sort(lst)
    print(lst)
    assert llst == lst
