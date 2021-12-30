import random


class ListNode(object):
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.forwards = []


class SkipList(object):

    def __init__(self, max_level=4):
        self.max_level = max_level
        self.level = 1
        self.head = ListNode(None, None)
        self.head.forwards = [None] * max_level

    def __getitem__(self, k):
        p = self.head
        for i in range(self.level-1, -1, -1):
            while p.forwards[i] and p.forwards[i].k < k:
                p = p.forwards[i]
            if p.forwards[i] and p.forwards[i].k == k:
                return p.forwards[i].v

    def query(self, x, y):
        p = self.head
        begin = None
        for i in range(self.level-1, -1, -1):
            while p.forwards[i] and p.forwards[i].k < x:
                p = p.forwards[i]
            if p.forwards[i] and p.forwards[i].k >= x:
                begin = p.forwards[i]

        result = []
        if begin is None:
            return result

        while begin and begin.k <= y:
            result.append(begin.v)
            begin = begin.forwards[0]
        return result

    def __setitem__(self, k, v):
        level = self._random_level()
        if self.level < level:
            self.level = level

        node = ListNode(k, v)
        node.forwards = [None] * level
        update = [self.head] * level

        p = self.head
        for i in range(level-1, -1, -1):
            while p.forwards[i] and p.forwards[i].k < k:
                p = p.forwards[i]
            if p.forwards[i] and p.forwards[i].k == k:
                p.forwards[i].v = v
                return False
            update[i] = p

        for i in range(level):
            node.forwards[i] = update[i].forwards[i]
            update[i].forwards[i] = node

        return True

    def __delitem__(self, k):
        update = [None] * self.level
        p = self.head
        for i in range(self.level-1, -1, -1):
            while p.forwards[i] and p.forwards[i].k < k:
                p = p.forwards[i]
            update[i] = p

        if p.forwards[0] and p.forwards[0].k == k:
            for i in range(self.level-1, -1, -1):
                if update[i].forwards[i] and update[i].forwards[i].k == k:
                    update[i].forwards[i] = update[i].forwards[i].forwards[i]
            return True

        return False

    def _random_level(self, p=0.5):
        level = 1
        while random.random() < p and level < self.max_level:
            level += 1

        return level

    def pprint(self):
        for i in range(self.level-1, -1, -1):
            p = self.head
            while p:
                print("{}:{}->".format(p.k, p.v), end="")
                p = p.forwards[i]
            print("")


if __name__ == '__main__':
    s = SkipList()
    s['c'] = 3
    s['d'] = 4
    s['a'] = 1
    s['e'] = 5
    s['f'] = 6
    s['b'] = 2
    s['g'] = 7
    s['h'] = 8
    s['i'] = 9
    s.pprint()

    print("")
    del s['a']
    s.pprint()

    assert s['b'] == 2

    print(s.query('d', 'f'))
