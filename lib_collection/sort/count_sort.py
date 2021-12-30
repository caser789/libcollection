def sort(lst):
    """
    >>> lst = [2, 5, 3, 0, 2, 3, 0, 3]
    >>> sort(lst)
    >>> lst
    []
    """
    if not lst:
        return

    # 1. get max (5)
    _max = lst[0]
    for v in lst:
        if v > _max:
            _max = v

    # 2. count ([2, 0, 2, 3, 0, 1])
    counter = [0 for _ in range(_max+1)]
    for v in lst:
        counter[v] += 1

    # 3. prefix sum (the largest index of the number)
    # [2, 2, 4, 7, 7, 8]
    for i in range(1, _max+1):
        counter[i] += counter[i-1]

    # insert number by order
    tmp = lst[:]
    for i in range(len(lst)-1, -1, -1):
        v = tmp[i]
        j = counter[v]-1
        counter[v] -= 1
        lst[j] = v


import random

for _ in range(20):
    lst = [random.randint(1, 100) for _ in range(20)]
    llst = sorted(lst)
    sort(lst)
    assert llst == lst
    print(lst)
