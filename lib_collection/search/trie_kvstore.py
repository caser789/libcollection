class Node(object):
    def __init__(self, val, capacity=26):
        self.val = val
        self.children = [None] * capacity


class Trie(object):

    def __init__(self, capacity=26):
        self.capacity = capacity
        self.root = None

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

    def _get_node(self, node, key, level):
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

        if level == len(key):
            return node

        c = key[level]
        i = ord(c) - ord('a')
        return self._get_node(node.children[i], key, level+1)
