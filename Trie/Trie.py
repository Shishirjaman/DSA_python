class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                current_node.children[c] = TrieNode()
            current_node = current_node.children[c]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for c in word:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return current_node.is_end_of_word

    def delete(self, word):
        self._delete(self.root, word, 0)

    def has_prefix(self, prefix):
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return False
            current_node = current_node.children[c]
        return True

    def starts_with(self, prefix):
        words = []
        current_node = self.root
        for c in prefix:
            if c not in current_node.children:
                return words
            current_node = current_node.children[c]
        def _dfs(node, path):
            if node.is_end_of_word:
                words.append(''.join(path))
            for char, child in node.children.items():
                _dfs(child, path + [char])
        _dfs(current_node, list(prefix))
        return words

    def list_words(self):
        words = []
        def _dfs(node, path):
            if node.is_end_of_word:
                words.append(''.join(path))
            for char, child in node.children.items():
                _dfs(child, path + [char])
        _dfs(self.root, [])
        return words

    def count_words(self):
        def dfs(node):
            total = 1 if node.is_end_of_word else 0
            for child in node.children.values():
                total += dfs(child)
            return total
        return dfs(self.root)

    def count_prefix(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children:
                return 0
            node = node.children[c]
        def dfs(n):
            total = 1 if n.is_end_of_word else 0
            for child in n.children.values():
                total += dfs(child)
            return total
        return dfs(node)

    def longest_prefix(self, word):
        node = self.root
        longest = ''
        curr_prefix = ''
        for c in word:
            if c not in node.children:
                break
            node = node.children[c]
            curr_prefix += c
            if node.is_end_of_word:
                longest = curr_prefix
        return longest

    def find_words_with_wildcard(self, pattern):
        result = []
        def dfs(node, index, path):
            if index == len(pattern):
                if node.is_end_of_word:
                    result.append(''.join(path))
                return
            c = pattern[index]
            if c == '.':
                for char, child in node.children.items():
                    dfs(child, index + 1, path + [char])
            elif c in node.children:
                dfs(node.children[c], index + 1, path + [c])
        dfs(self.root, 0, [])
        return result

    def autocomplete(self, prefix, limit=None):
        results = []
        node = self.root
        for c in prefix:
            if c not in node.children:
                return results
            node = node.children[c]
        def dfs(current, path):
            if current.is_end_of_word:
                results.append(''.join(path))
                if limit is not None and len(results) >= limit:
                    return True
            for char, child in current.children.items():
                if dfs(child, path + [char]):
                    return True
            return False
        dfs(node, list(prefix))
        return results

    def _delete(self, current_node, word, index):
        if index == len(word):
            if not current_node.is_end_of_word:
                return False
            current_node.is_end_of_word = False
            return len(current_node.children) == 0
        c = word[index]
        node = current_node.children.get(c)
        if node is None:
            return False
        delete_curr_node = self._delete(node, word, index+1)
        if delete_curr_node:
            del current_node.children[c]
            return len(current_node.children) == 0 and not current_node.is_end_of_word
        return False



if __name__ == "__main__":
    trie = Trie()
    trie.insert('hello')
    trie.insert('henry')
    trie.insert('mike')
    trie.insert('minimal')
    trie.insert('minimum')
    trie.insert('mini')

    print("All words:", trie.list_words())
    print("Has prefix 'mi'?", trie.has_prefix('mi'))
    print("Words starting with 'mi':", trie.starts_with('mi'))
    print("Total words:", trie.count_words())
    print("Words with prefix 'mi':", trie.count_prefix('mi'))
    print("Longest prefix of 'minimize':", trie.longest_prefix('minimize'))
    print("Wildcard '.in.':", trie.find_words_with_wildcard('.in.'))
    print("Autocomplete for 'mi' (limit 2):", trie.autocomplete('mi', 2))

    trie.delete('minimal')
    print("After deleting 'minimal', words starting with 'mi':", trie.starts_with('mi'))
    print("Search for 'minimum':", trie.search('minimum'))
    print("Search for 'minimal':", trie.search('minimal'))
    print("Search for 'mini':", trie.search('mini'))
    trie.insert('minimize')
    print("Autocomplete for 'min':", trie.autocomplete('min'))