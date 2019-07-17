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
        """
        >>> s = LinkedStack()
        >>> len(s)
        0
        >>> s.push('a')
        >>> s.push('b')
        >>> len(s)
        2
        >>> s.pop()
        'b'
        >>> len(s)
        1
        """
        return self.n

    def __contains__(self, i):
        """
        >>> s = LinkedStack()
        >>> s.push('a')
        >>> s.push('b')
        >>> 'a' in s
        True
        >>> 'c' in s
        False
        """
        for j in self:
            if j == i:
                return True
        return False

    def __iter__(self):
        """
        >>> s = LinkedStack()
        >>> s.push('a')
        >>> s.push('b')
        >>> s.push('c')
        >>> for i in s:
        ...     print i
        ...
        c
        b
        a
        """
        n = self.head.next
        while n:
            yield n.v
            n = n.next

    def __str__(self):
        """
        >>> s = LinkedStack()
        >>> s.push('a')
        >>> s.push(2)
        >>> s.push('c')
        >>> s
        LinkedStack(['c', 2, 'a'])
        >>> print s
        LinkedStack(['c', 2, 'a'])
        """
        return 'LinkedStack([{}])'.format(', '.join(repr(i) for i in self))

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
        """
        >>> s = LinkedStack()
        >>> s.push('a')
        >>> s.push('b')
        >>> s.pop()
        'b'
        >>> s.pop()
        'a'
        >>> s.pop()
        Traceback (most recent call last):
            ...
        IndexError: pop from empty stack
        """
        if len(self) == 0:
            raise IndexError('pop from empty stack')
        res = self.head.next.v
        self.head.next = self.head.next.next
        self.n -= 1
        return res

    @property
    def top(self):
        """
        >>> s = LinkedStack()
        >>> s.top
        Traceback (most recent call last):
            ...
        IndexError: pop from empty stack
        >>> s.push('a')
        >>> s.top
        'a'
        """
        if len(self) == 0:
            raise IndexError('pop from empty stack')
        return self.head.next.v
