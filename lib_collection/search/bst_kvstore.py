class Node(object):
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.left = None
        self.right = None
        self.size = 1

    def __repr__(self):
        """
        >>> n = Node(1, 'a')
        >>> n
        Node(1, 'a')
        """
        return 'Node({}, {})'.format(repr(self.k), repr(self.v))


class BSTKVStore(object):

    def __init__(self):
        self.root = None
        self.n = 0

    def __setitem__(self, k, v):
        """
        >>> s = BSTKVStore()
        >>> s[2] = 'b'
        >>> s.root
        Node(2, 'b')
        >>> s[1] = 'a'
        >>> s.root.left
        Node(1, 'a')
        >>> s[3] = 'c'
        >>> s.root.right
        Node(3, 'c')
        """
        self.root = self._put_to_node(self.root, k, v)

    def __getitem__(self, k):
        n = self._get_node(self.root, k)
        return n.v if n else None

    def __len__(self):
        return self._get_size(self.root)

    def _put_to_node(self, node, k, v):
        if node is None:
            return Node(k, v)

        if node.k == k:
            node.v = v
        elif k < node.k:
            node.left = self._put_to_node(node.left, k, v)
        else:
            node.right = self._put_to_node(node.right, k, v)

        node.size = 1 + self._get_size(node.left) + self._get_size(node.right)
        return node

    def _get_size(self, node):
        if node is None:
            return 0
        return node.size

    def _get_node(self, node, k):
        """
        >>> # 1. test the node passed in is None
        >>> s = BSTKVStore()
        >>> n = s._get_node(None, 'k')
        >>> n

        >>> # 2. test k equal
        >>> s = BSTKVStore()
        >>> n = Node(1, 'a')
        >>> res = s._get_node(n, 1)
        >>> res is n
        True
        >>> # 3. test k less than k of node and found
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> a = Node(1, 'a')
        >>> b.left = a
        >>> res = s._get_node(b, 1)
        >>> res is a
        True
        >>> # 4. test k less than k of node and not found
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> a = Node(1, 'a')
        >>> b.left = a
        >>> res = s._get_node(b, 1.5)
        >>> res is None
        True
        >>> # 5. test k greater than k of node and found
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> c = Node(3, 'c')
        >>> b.right = c
        >>> res = s._get_node(b, 3)
        >>> res is c
        True
        >>> # 5. test k greater than k of node and not found
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> c = Node(3, 'c')
        >>> b.right = c
        >>> res = s._get_node(b, 2.5)
        >>> res is None
        True
        """
        if not node:
            return

        if node.k == k:
            return node

        if k < node.k:
            return self._get_node(node.left, k)

        return self._get_node(node.right, k)