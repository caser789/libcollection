BLACK = False
RED = True


class Node(object):
    def __init__(self, k, v, color):
        self.k = k
        self.v = v
        self.color = color
        self.size = 1
        self.left = None
        self.right = None


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

        >>> t = RedBlackTree()
        >>> node = Node('b', 2, BLACK)
        >>> node = t._set_node(node, 'a', 1)
        >>> node.k == 'b'
        True
        >>> node.color is BLACK
        True
        >>> node.left.k == 'a'
        True
        >>> node.left.color is RED
        True

        >>> t = RedBlackTree()
        >>> node = Node('b', 2, BLACK)
        >>> node = t._set_node(node, 'c', 3)
        >>> node.k == 'c'
        True
        >>> node.color is BLACK
        True
        >>> node.left.k == 'b'
        True
        >>> node.left.color is RED
        True

        >>> node = t._set_node(node, 'd', 4)
        >>> node.k == 'c'
        True
        >>> node.color is RED
        True
        >>> node.left.k == 'b'
        True
        >>> node.left.color is BLACK
        True
        >>> node.right.k == 'd'
        True
        >>> node.right.color is BLACK
        True

        >>> t = RedBlackTree()
        >>> node = None
        >>> node = t._set_node(node, 'c', 3)
        >>> node.color = BLACK
        >>> node = t._set_node(node, 'b', 2)
        >>> node = t._set_node(node, 'a', 1)
        >>> node.k == 'b'
        True
        >>> node.color is RED
        True
        >>> node.left.k == 'a'
        True
        >>> node.left.color is BLACK
        True
        >>> node.right.k == 'c'
        True
        >>> node.right.color is BLACK
        True
        """
        if node is None:
            return Node(k, v, RED)

        if node.k == k:
            node.v = v
        elif k < node.k:
            node.left = self._set_node(node.left, k, v)
        else:
            node.right = self._set_node(node.right, k, v)

        if self._is_red(node.right) and not self._is_red(node.left):
            node = self._rotate_left(node)

        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)

        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_color(node)

        node.size = self._size(node.left) + self._size(node.right) + 1
        return node

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

    def _size(self, node):
        """
        >>> t = RedBlackTree()
        >>> node = None
        >>> t._size(node)
        0
        >>> node = Node('a', 1, RED)
        >>> node.size
        1
        >>> t._size(node)
        1
        >>> node.size = 2
        >>> t._size(node)
        2
        """
        if node is None:
            return 0
        return node.size

    def _is_red(self, node):
        """
        >>> t = RedBlackTree()
        >>> node = None
        >>> t._is_red(node)
        False
        >>> node = Node('a', 1, RED)
        >>> t._is_red(node)
        True
        >>> node.color = BLACK
        >>> t._is_red(node)
        False
        """
        if node is None:
            return False
        return node.color is RED

    def _rotate_left(self, node):
        """
        >>> t = RedBlackTree()
        >>> x = Node('a', 1, BLACK)
        >>> y = Node('b', 2, RED)
        >>> x.right = y
        >>> x.size = 2
        >>> z = t._rotate_left(x)
        >>> z is y
        True
        >>> z.left is x
        True
        >>> z.color is BLACK
        True
        >>> z.left.color is RED
        True
        >>> z.size == 2
        True
        >>> z.left.size == 1
        True
        """
        assert node is not None and self._is_red(node.right)
        x = node
        y = node.right

        x.right = y.left
        y.left = x
        y.color = x.color
        x.color = RED

        y.size = x.size
        x.size = self._size(x.left) + self._size(x.right) + 1
        return y

    def _rotate_right(self, node):
        """
        >>> t = RedBlackTree()
        >>> y = Node('b', 1, BLACK)
        >>> x = Node('a', 0, RED)
        >>> y.left = x
        >>> y.size = 2
        >>> z = t._rotate_right(y)
        >>> z is x
        True
        >>> z.right is y
        True
        >>> z.color is BLACK
        True
        >>> z.right.color is RED
        True
        >>> z.size == 2
        True
        >>> z.right.size == 1
        True
        """
        assert node is not None and self._is_red(node.left)
        x = node.left
        y = node

        y.left = x.right
        x.right = y
        x.color = y.color
        y.color = RED

        x.size = y.size
        y.size = self._size(y.left) + self._size(y.right) + 1
        return x

    def _flip_color(self, node):
        """
        >>> x = Node('a', 1, RED)
        >>> y = Node('b', 2, BLACK)
        >>> z = Node('c', 3, RED)
        >>> y.left = x
        >>> y.right = z
        >>> t = RedBlackTree()
        >>> a = t._flip_color(y)
        >>> y.color is RED
        True
        >>> x.color is BLACK
        True
        >>> z.color is BLACK
        True
        """
        assert node is not None
        assert node.left is not None
        assert node.right is not None
        assert node.color != node.left.color
        assert node.color != node.right.color
        node.color = not node.color
        node.left.color = not node.left.color
        node.right.color = not node.right.color

    def delete_max(self):
        if self.root is None:
            return

        if not self._is_red(self.root.left) and not self._is_red(self.root.right):
            self.root.color = RED

        self.root = self._del_max_node(self.root)

        if self.root is not None:
            self.root.color = BLACK

    def _del_max_node(self, node):
        if self._is_red(node.left):
            node = self._rotate_right(node)

        if node.right is None:
            return

        if not self._is_red(node.left) and not self._is_red(node.right):
            node = self._move_red_right(node)

        node.right = self._del_max_node(node.right)
        return self._balance(node)

    def _balance(self, node):
        assert node is not None

        if self._is_red(node.right):
            node = self._rotate_left(node)

        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self._rotate_right(node)

        if self._is_red(node.left) and self._is_red(node.right):
            self._flip_color(node)

        node.size = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _move_red_right(self, node):
        assert node is not None
        assert self._is_red(node)
        assert not self._is_red(node.left)
        assert not self._is_red(node.right)
        self._flip_color(node)
        if self._is_red(node.left.left):
            node = self._rotate_right(node)
            self._flip_color(node)
        return node

    def delete_min(self):
        if self.root is None:
            return

        if not self._is_red(self.root.left) and not self._is_red(self.root.right):
            self.root.color = RED

        self.root = self._del_min_node(self.root)

        if self.root is not None:
            self.root.color = BLACK

    def _del_min_node(self, node):
        if node.left is None:
            return

        if not self._is_red(node.left) and not self._is_red(node.left.left):
            node = self._move_red_left(node)

        node.left = self._del_min_node(node.left)
        return self._balance(node)

    def _move_red_left(self, node):
        assert node is not None
        assert self._is_red(node)
        assert not self._is_red(node.left)
        assert not self._is_red(node.right)

        self._flip_color(node)
        if self._is_red(node.right.left):
            node.right = self._rotate_right(node.right)
            node = self._rotate_left(node)
            self._flip_color(node)
        return node

    def __delitem__(self, k):
        if self.root is None:
            return

        if not self._is_red(self.root.left) and not self._is_red(self.root.right):
            self.root.color = RED

        self.root = self._del_node(self.root, k)

        if self.root is not None:
            self.root.color = BLACK

    def _del_node(self, node, k):
        if k < node.k:
            if not self._is_red(node.left) and not self._is_red(node.left.left):
                node = self._move_red_left(node)
            node.left = self._del_node(node.left, k)
        else:
            if self._is_red(node.left):
                node = self._rotate_right(node)

            if k == node.k and node.right is None:
                return

            if not self._is_red(node.right) and not self._is_red(node.right.left):
                node = self._move_red_right(node)

            if k == node.k:
                x = self._get_min_node(node.right)
                node.k = x.k
                node.v = x.v
                node.right = self._del_min_node(node.right)
            else:
                node.right = self._del_node(node.right, k)
        return self._balance(node)

    def _get_min_node(self, node):
        if node.left is None:
            return node
        return self._get_min_node(node.left)
