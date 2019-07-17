class Node(object):
    def __init__(self, v):
        self.v = v
        self.next = None

    def __str__(self):
        """
        >>> n = Node('a')
        >>> n
        Node('a')
        >>> n = Node(1)
        >>> n
        Node(1)
        """
        return 'Node({})'.format(repr(self.v))

    __repr__ = __str__


class LinkedStack(object):

    def __init__(self):
        self.n = 0
        self.head = Node(None)

    def __len__(self):
        return self.n

    def __contains__(self):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        pass

    __repr__ = __str__

    def push(self, i):
        """
        >>> s = LinkedStack()
        >>> s.push('a')
        """
        n = Node(i)
        n.next = self.head.next
        self.head.next = n
        self.n += 1

    def pop(self):
        pass

    @property
    def top(self):
        pass
