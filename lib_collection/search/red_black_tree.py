BLACK = False
RED = True


class Node(object):
    def __init__(self, k, v, color):
        self.k = k
        self.v = v
        self.color = color
        self.size = 1


class RedBlackTree(object):
    def __init__(self):
        self.root = None

    def __setitem__(self, k, v):
        """
        >>> t = RedBlackTree()
        >>> t['a'] = 1
        >>> t.root.k == 'a'
        True
        >>> t.root.v == 1
        True
        >>> t.root.color == BLACK
        True
        """
        self.root = self._set_node(self.root, k, v)
        self.root.color = BLACK

    def _set_node(self, node, k, v):
        """
        >>> t = RedBlackTree()
        >>> node = None
        >>> mode = t._set_node(node, 'a', 1)
        >>> mode.k == 'a'
        True
        >>> mode.v == 1
        True
        >>> mode.color == BLACK
        False
        """
        if node is None:
            return Node(k, v, RED)

    def __len__(self):
        """
        >>> t = RedBlackTree()
        >>> len(t)
        0
        >>> t['a'] = 1
        >>> len(t)
        1
        """
        return self.root.size if self.root is not None else 0
