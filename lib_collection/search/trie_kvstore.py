class Node(object):
    def __init__(self, val, capacity=26):
        self.val = val
        self.children = [None] * capacity


class Trie(object):

    def __init__(self, capacity=26):
        self.capacity = capacity
        self.root = None
        self.n = 0

    def __getitem__(self, key):
        """
        >>> t = Trie()
        >>> t['a'] is None
        True
        >>> t = Trie()
        >>> node = Node(None)
        >>> node.children[0] = Node(1)
        >>> t.root = node
        >>> t['a'] == 1
        True
        """
        node = self._get_node(self.root, key, 0)
        if node is not None:
            return node.val

    def _get_node(self, node, key, index):
        """
        >>> t = Trie()
        >>> n = t._get_node(t.root, 'a', 1)
        >>> n is None
        True
        >>> t = Trie()
        >>> node = Node('ab')
        >>> n = t._get_node(node, 'cd', 2)
        >>> n is node
        True
        >>> t = Trie()
        >>> node_a = Node('a')
        >>> node_b = Node('b')
        >>> index = ord('e') - ord('a')
        >>> node_a.children[index] = node_b
        >>> n = t._get_node(node_a, 'cde', 2)
        >>> n is node_b
        True
        """
        if node is None:
            return

        if index == len(key):
            return node

        c = key[index]
        i = ord(c) - ord('a')
        return self._get_node(node.children[i], key, index+1)

    def __setitem__(self, key, val):
        self.root = self._set_node(self.root, key, val, 0)

    def _set_node(self, node, key, val, index):
        """
        >>> t = Trie()
        >>> node = t._set_node(t.root, 'ab', 12, 2)
        >>> node.val == 12
        True
        >>> t = Trie()
        >>> node = t._set_node(t.root, 'ab', 12, 0)
        >>> node.children[0].children[1].val == 12
        True
        """
        if node is None:
            node = Node(None)

        if index == len(key):
            if node.val is None:
                self.n += 1
            node.val = val
            return node

        c = key[index]
        i = ord(c) - ord('a')
        node.children[i] = self._set_node(node.children[i], key, val, index+1)
        return node
