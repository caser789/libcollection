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
        """
        >>> # 1. test KeyError
        >>> s = BSTKVStore()
        >>> s[5]
        Traceback (most recent call last):
            ...
        KeyError: 5
        >>> # 2. test found
        >>> s[1] = 'a'
        >>> s[2] = 'b'
        >>> s[3] = 'c'
        >>> s[3]
        'c'
        >>> s[2]
        'b'
        >>> s[1]
        'a'
        """
        n = self._get_node(self.root, k)
        if n is None:
            raise KeyError(k)
        return n.v

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

    @property
    def min(self):
        """
        >>> # 1. test index error
        >>> s = BSTKVStore()
        >>> s.min
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> # 2. test get min
        >>> s = BSTKVStore()
        >>> s[2] = 'b'
        >>> s[1] = 'a'
        >>> s[3] = 'c'
        >>> s.min
        1
        """
        if len(self) == 0:
            raise IndexError('underflow')
        n = self._get_min_node(self.root)
        return n.k

    def _get_min_node(self, node):
        """
        >>> # 1. test node is the min node
        >>> s = BSTKVStore()
        >>> b = Node(1, 'b')
        >>> n = s._get_min_node(b)
        >>> n is b
        True
        >>> # 2. test node is not the min node
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> a = Node(1, 'a')
        >>> b.left = a
        >>> n = s._get_min_node(b)
        >>> n is a
        True
        """
        if node.left is None:
            return node
        return self._get_min_node(node.left)

    def _get_max_node(self, node):
        """
        >>> # 1. test node is the max node
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> n = s._get_max_node(b)
        >>> n is b
        True
        >>> # 2. test node is not the max node
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> c = Node(3, 'c')
        >>> b.right = c
        >>> n = s._get_max_node(b)
        >>> n is c
        True
        """
        if node.right is None:
            return node
        return self._get_max_node(node.right)

    @property
    def max(self):
        """
        >>> # 1. test index error
        >>> s = BSTKVStore()
        >>> s.max
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> # 2. test get max
        >>> s = BSTKVStore()
        >>> s[2] = 'b'
        >>> s[3] = 'c'
        >>> s[1] = 'a'
        >>> s.max
        3
        """
        if len(self) == 0:
            raise IndexError('underflow')
        n = self._get_max_node(self.root)
        return n.k

    def delete_min(self):
        """
        >>> # 1. test index error
        >>> s = BSTKVStore()
        >>> s.delete_min()
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> # 2. test delete min
        >>> s = BSTKVStore()
        >>> s[2] = 'b'
        >>> s[3] = 'c'
        >>> s[1] = 'a'
        >>> s.min
        1
        >>> s.delete_min()
        >>> s.min
        2
        >>> s.delete_min()
        >>> s.min
        3
        """
        if len(self) == 0:
            raise IndexError('underflow')
        self.root = self._delete_min_node(self.root)

    def _delete_min_node(self, node):
        """
        >>> # 1. node is the min node
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> c = Node(3, 'c')
        >>> b.right = c
        >>> n = s._delete_min_node(b)
        >>> n is c
        True
        >>> # 1. node is not the min node
        >>> s = BSTKVStore()
        >>> a = Node(1, 'a')
        >>> b = Node(2, 'b')
        >>> c = Node(3, 'c')
        >>> b.left = a
        >>> b.right = c
        >>> n = s._delete_min_node(b)
        >>> n is b
        True
        >>> n.left is None
        True
        """
        if node.left is None:
            return node.right
        node.left = self._delete_min_node(node.left)
        node.size = 1 + self._get_size(node.left) + self._get_size(node.right)
        return node

    def _delete_max_node(self, node):
        """
        >>> # 1. node is the max node
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> a = Node(1, 'd')
        >>> b.left = a
        >>> n = s._delete_max_node(b)
        >>> n is a
        True
        >>> # 2. node is not the max node
        >>> s = BSTKVStore()
        >>> a = Node(1, 'a')
        >>> b = Node(2, 'b')
        >>> c = Node(3, 'c')
        >>> b.left = a
        >>> b.right = c
        >>> n = s._delete_max_node(b)
        >>> n is b
        True
        >>> n.right is None
        True
        """
        if node.right is None:
            return node.left
        node.right = self._delete_max_node(node.right)
        node.size = 1 + self._get_size(node.left) + self._get_size(node.right)
        return node

    def delete_max(self):
        """
        >>> # 1. test index error
        >>> s = BSTKVStore()
        >>> s.delete_max()
        Traceback (most recent call last):
            ...
        IndexError: underflow
        >>> # 2. test delete max
        >>> s = BSTKVStore()
        >>> s[2] = 'b'
        >>> s[3] = 'c'
        >>> s[1] = 'a'
        >>> s.max
        3
        >>> s.delete_max()
        >>> s.max
        2
        >>> s.delete_max()
        >>> s.max
        1
        """
        if len(self) == 0:
            raise IndexError('underflow')
        self.root = self._delete_max_node(self.root)

    def __delitem__(self, k):
        """
        >>> s = BSTKVStore()
        >>> s[2] = 'b'
        >>> s[3] = 'c'
        >>> s[1] = 'a'
        >>> s[3]
        'c'
        >>> del s[3]
        >>> s[3]
        Traceback (most recent call last):
            ...
        KeyError: 3
        """
        self.root = self._delete_node(self.root, k)

    def _delete_node(self, node, k):
        """
        >>> # 1. test node is None
        >>> s = BSTKVStore()
        >>> res = s._delete_node(None, 'k')
        >>> res is None
        True
        >>> # 2. test k < node.k
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> a = Node(1, 'a')
        >>> n = s._delete_node(b, 1)
        >>> n is b
        True
        >>> n.left is None
        True
        >>> # 3. test k > node.k
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> c = Node(3, 'c')
        >>> n = s._delete_node(b, 3)
        >>> n is b
        True
        >>> n.right is None
        True
        >>> # 4. test k == node.k
        >>> s = BSTKVStore()
        >>> a = Node(1, 'a')
        >>> b = Node(2, 'b')
        >>> c = Node(3, 'c')
        >>> b.left = a
        >>> b.right = c
        >>> n = s._delete_node(b, 2)
        >>> n is c
        True
        >>> n.left is a
        True
        """
        if node is None:
            return

        if k < node.k:
            node.left = self._delete_node(node.left, k)
        elif k > node.k:
            node.right = self._delete_node(node.right, k)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            n = self._get_min_node(node.right)
            n.right = self._delete_min_node(node.right)
            n.left = node.left
            node = n

        node.size = 1 + self._get_size(node.left) + self._get_size(node.right)
        return node

    def floor(self, k):
        """
        Return the largest key <= k
        """
        n = self._get_floor_node(self.root, k)
        return n.k if n else None

    def _get_floor_node(self, node, k):
        """
        Return the largest node with key <= k
        >>> # 1. test node is None
        >>> s = BSTKVStore()
        >>> n = s._get_floor_node(None, 'k')
        >>> n is None
        True
        >>> # 2. test node.k == k
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> n = s._get_floor_node(b, 2)
        >>> n is b
        True
        >>> # 3. test k  < node.k
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> a = Node(1, 'a')
        >>> b.left = a
        >>> n = s._get_floor_node(b, 1.5)
        >>> n is a
        True
        >>> # 4. test k < node.k
        >>> s = BSTKVStore()
        >>> a = Node(1, 'a')
        >>> b = Node(2, 'b')
        >>> c = Node(3, 'c')
        >>> b.left = a
        >>> b.right = c
        >>> n = s._get_floor_node(b, 3)
        >>> n is c
        True
        >>> # 5. test k < node.k and not found in right
        >>> s = BSTKVStore()
        >>> a = Node(1, 'a')
        >>> b = Node(2, 'b')
        >>> c = Node(3, 'c')
        >>> b.left = a
        >>> b.right = c
        >>> n = s._get_floor_node(b, 2.5)
        >>> n is b
        True
        >>> # 6. test k  < node.k and not found in left
        >>> s = BSTKVStore()
        >>> b = Node(2, 'b')
        >>> n = s._get_floor_node(b, 1.5)
        >>> n is None
        True
        """
        if not node:
            return
        if node.k == k:
            return node

        if k < node.k:
            return self._get_floor_node(node.left, k)

        n = self._get_floor_node(node.right, k)
        if not n:
            return node
        return n
