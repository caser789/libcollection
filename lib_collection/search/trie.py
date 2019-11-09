class TrieNode(object):

    def __init__(self, val, r=26):
        self.val = val
        self.children = [None] * r


class Trie(object):

    def __init__(self):
        self.root = TrieNode(None)
        self.n = 0

    def __setitem__(self, key, val):
        if val is None:
            del self[key]

        self.root = self._setnode(self.root, key, val, 0)

    def _setnode(self, node, key, val, i):
        if node is None:
            node = TrieNode(None)

        if len(key) == i:
            if node.val is None:
                self.n += 1
            node.val = val
            return node

        j = ord(key[i]) - ord('a')
        node.children[j] = self._setnode(node.children[j], key, val, i+1)
        return node

    def __getitem__(self, key):
        node = self._getnode(self.root, key, 0)
        if node:
            return node.val

    def _getnode(self, node, key, i):
        if node is None:
            return

        if i == len(key):
            return node

        j = ord(key[i]) - ord('a')

        return self._getnode(node.children[j], key, i+1)

    def __delitem__(self, key):
        self.root = self._delnode(self.root, key, 0)

    def _delnode(self, node, key, i):
        if node is None:
            return

        if i == len(key):
            if node.val is not None:
                self.n -= 1
            node.val = None
        else:
            j = ord(key[i]) - ord('a')
            node.children[j] = self._delnode(node.children[j], key, i+1)

        if node.val is not None:
            return node

        for i in range(len(node.children)):
            if node.children[i] is not None:
                return node

    def __len__(self):
        return self.n

    def __contains__(self, key):
        node = self._getnode(self.root, key, 0)
        return node is not None

    def keys(self):
        return self.keys_with_prefix("")

    def keys_with_prefix(self, prefix):
        keys = []
        node = self._getnode(self.root, prefix, 0)
        tmp = []
        self.collect(node, tmp, keys)
        return keys

    def collect(self, node, tmp, keys):
        if node is None:
            return
        if node.val is not None:
            keys.append(''.join(tmp))

        for i in range(len(node.children)):
            tmp.append(chr(ord('a')+i))
            self.collect(node.children[i], tmp, keys)
            tmp.pop()
