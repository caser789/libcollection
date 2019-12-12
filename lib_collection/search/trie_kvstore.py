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
        """
        >>> t = Trie()
        >>> t['ab'] = 12
        >>> t['ab']
        12
        """
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

    def __delitem__(self, key):
        """
        >>> t = Trie()
        >>> del t['a']
        >>> t['a'] = 1
        >>> t['a']
        1
        >>> del t['a']
        >>> t['a'] is None
        True
        """
        self.root = self._del_node(self.root, key, 0)

    def _del_node(self, node, key, index):
        """
        >>> t = Trie()
        >>> node = t._del_node(None, 'ab', 2)
        >>> node is None
        True
        >>> t = Trie()
        >>> node = Node(12)
        >>> node = t._del_node(node, 'ab', 2)
        >>> node is None
        True
        >>> t.n
        -1
        >>> t = Trie()
        >>> node = Node(12)
        >>> node_2 = Node(34)
        >>> node.children[0] = node_2
        >>> node3 = t._del_node(node, 'ab', 2)
        >>> node3 is None
        False
        >>> node3 is node
        True
        >>> t.n
        -1
        >>> t = Trie()
        >>> node = Node(12)
        >>> node_2 = Node(34)
        >>> node.children[2] = node_2
        >>> node3 = t._del_node(node, 'abc', 2)
        >>> node3 is node
        True
        >>> node3.children[2] is None
        True
        >>> t.n
        -1
        """
        if node is None:
            return

        if index == len(key):
            if node.val is not None:
                self.n -= 1
                node.val = None
        else:
            c = key[index]
            i = ord(c) - ord('a')
            node.children[i] = self._del_node(node.children[i], key, index+1)

        if node.val is not None:
            return node

        for c in node.children:
            if c is not None:
                return node
        return None

    def keys(self):
        """
        >>> t = Trie()
        >>> t['abc'] = 1
        >>> t['abcd'] = 2
        >>> t['abce'] = 3
        >>> t['ax'] = 4
        >>> t.keys()
        ['abc', 'abcd', 'abce', 'ax']
        """
        return self.keys_with_prefix("")

    def keys_with_prefix(self, prefix):
        """
        >>> t = Trie()
        >>> t['abc'] = 1
        >>> t['abcd'] = 2
        >>> t['abce'] = 3
        >>> t['ax'] = 4
        >>> t.keys_with_prefix('ab')
        ['abc', 'abcd', 'abce']
        """
        node = self._get_node(self.root, prefix, 0)
        res = []
        self._collect(node, list(prefix), res)
        return res

    def _collect(self, node, chars, res):
        """
        >>> t = Trie()
        >>> res = []
        >>> t._collect(None, ['a', 'b'], res)
        >>> not res
        True
        >>> t = Trie()
        >>> node = Node(12)
        >>> res = []
        >>> t._collect(node, ['a', 'b'], res)
        >>> res
        ['ab']
        >>> t = Trie()
        >>> res = []
        >>> node = Node(None)
        >>> node.children[2] = Node(11)
        >>> t._collect(node, ['a', 'b'], res)
        >>> res
        ['abc']
        """
        if node is None:
            return

        if node.val is not None:
            res.append(''.join(chars))

        for i in range(len(node.children)):
            c = chr(ord('a') + i)
            chars.append(c)
            self._collect(node.children[i], chars, res)
            chars.pop()

    def keys_with_pattern(self, pattern):
        """
        >>> t = Trie()
        >>> t['a'] = 1
        >>> t['ab'] = 2
        >>> t['ac'] = 3
        >>> t['acd'] = 3
        >>> t.keys_with_pattern('a.')
        ['ab', 'ac']
        >>> t.keys_with_pattern('acd')
        ['acd']
        """
        res = []
        self._collect_with_pattern(self.root, [], pattern, res)
        return res

    def _collect_with_pattern(self, node, chars, pattern, res):
        """
        >>> t = Trie()
        >>> node = t._collect_with_pattern(None, ['a', 'c'], 'ac', [])
        >>> node is None
        True
        >>> t = Trie()
        >>> node = Node(1)
        >>> res = []
        >>> t._collect_with_pattern(node, ['a', 'c'], 'de', res)
        >>> res
        ['ac']
        >>> t = Trie()
        >>> node = Node(None)
        >>> res = []
        >>> t._collect_with_pattern(node, ['a', 'c'], 'de', res)
        >>> res
        []
        >>> t = Trie()
        >>> node = Node(None)
        >>> res = []
        >>> t._collect_with_pattern(node, ['a', 'c'], 'def', res)
        >>> res
        []
        >>> t = Trie()
        >>> node = Node(None)
        >>> node.children[5] = Node(1)
        >>> res = []
        >>> t._collect_with_pattern(node, ['a', 'c'], 'def', res)
        >>> res
        ['acf']
        >>> t = Trie()
        >>> node = Node(None)
        >>> node.children[5] = Node(1)
        >>> node.children[6] = Node(1)
        >>> res = []
        >>> t._collect_with_pattern(node, ['a', 'c'], 'de.', res)
        >>> res
        ['acf', 'acg']
        """
        if node is None:
            return

        d = len(chars)
        if d == len(pattern):
            if node.val is not None:
                res.append(''.join(chars))
            return

        c = pattern[d]
        if c == '.':
            for i in range(len(node.children)):
                ch = chr(ord('a')+i)
                chars.append(ch)
                self._collect_with_pattern(node.children[i], chars, pattern, res)
                chars.pop()
        else:
            chars.append(c)
            i = ord(c) - ord('a')
            self._collect_with_pattern(node.children[i], chars, pattern, res)
            chars.pop()
