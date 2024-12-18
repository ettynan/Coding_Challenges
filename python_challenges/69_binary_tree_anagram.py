class TreeNode:
    def __init__(self, key):
        self.key = key  # Canonical form (sorted word)
        self.anagrams = []  # List of anagrams
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, word):
        sorted_word = ''.join(sorted(word))  # Canonical form
        if not self.root:
            self.root = TreeNode(sorted_word)
            self.root.anagrams.append(word)
        else:
            self._insert_recursive(self.root, sorted_word, word)

    def _insert_recursive(self, node, sorted_word, word):
        if sorted_word == node.key:
            node.anagrams.append(word)
        elif sorted_word < node.key:
            if node.left is None:
                node.left = TreeNode(sorted_word)
                node.left.anagrams.append(word)
            else:
                self._insert_recursive(node.left, sorted_word, word)
        else:
            if node.right is None:
                node.right = TreeNode(sorted_word)
                node.right.anagrams.append(word)
            else:
                self._insert_recursive(node.right, sorted_word, word)

    def get_anagrams(self):
        result = []
        self._inorder_traversal(self.root, result)
        return [node.anagrams for node in result if len(node.anagrams) > 1]

    def _inorder_traversal(self, node, result):
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node)
            self._inorder_traversal(node.right, result)

# Example usage
words = ["listen", "silent", "enlist", "rat", "tar", "art", "god", "dog"]
tree = BinaryTree()

for word in words:
    tree.insert(word)

print("Anagram Groups:", tree.get_anagrams())
