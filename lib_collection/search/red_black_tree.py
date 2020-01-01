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
