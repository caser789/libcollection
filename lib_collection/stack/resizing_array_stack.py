class ResizingArrayStack(object):
    """
    This implementation uses a resizing array, which double the underlying array
    when it is full and halves the underlying array when it is one-quarter full.
    """

    def __init__(self):
        self.capacity = 2
        self.resizing_array = [None] * self.capacity
        self.n = 0

    def __len__(self):
        """
        >>> stack = ResizingArrayStack()
        >>> len(stack)
        0
        >>> stack.push('a')
        >>> len(stack)
        1
        """
        return self.n

    def __contains__(self, i):
        pass

    def __iter__(self):
        pass

    def __str__(self):
        """
        >>> stack = ResizingArrayStack()
        >>> stack.push('a')
        >>> stack.push('b')
        >>> stack
        ResizingArrayStack(['b', 'a'])
        """
        return 'ResizingArrayStack([{}])'.format(', '.join(e for e in self))

    __repr__ = __str__

    def push(self, item):
        """
        >>> stack = ResizingArrayStack()
        >>> stack.push('a')
        """
        self.resizing_array[self.n] = item
        self.n += 1

    def pop(self):
        """
        >>> stack = ResizingArrayStack()
        >>> stack.pop()
        Traceback (most recent call last):
            ...
        IndexError: pop from empty stack
        """
        if len(self) == 0:
            raise IndexError('pop from empty stack')
        self.n -= 1
        return self.resizing_array[self.n]

    @property
    def top(self):
        """
        >>> stack = ResizingArrayStack()
        >>> stack.top
        Traceback (most recent call last):
            ...
        IndexError: pop from empty stack
        """
        if len(self) == 0:
            raise IndexError('pop from empty stack')

    def _resize(self, m):
        pass
