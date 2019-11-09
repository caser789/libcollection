class TrieNode(object):

    def __init__(self, val, r=26):
        self.val = val
        self.children = [None] * r


class Trie(object):

    def __init__(self):
        self.root = TrieNode(None)

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
        pass

    def _delitem(self):
        pass

    def __len__(self):
        pass

    def __contains__(self, key):
        node = self._getnode(self.root, key, 0)
        return node is not None

    def __iter__(self):
        pass
