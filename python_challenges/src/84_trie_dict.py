'''Program to implement a Trie using a Dictionary'''

class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}  # Create a new node for the character if it doesn't exist
            node = node[char]
        node['end'] = True  # Mark the end of the word

    def search(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                return False  # Return False if the word is not found
            node = node[char]
        return 'end' in node  # Return True if the word ends here

    def starts_with(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node:
                return False  # Return False if the prefix is not found
            node = node[char]
        return True  # Return True if the prefix exists

# Example usage
trie = Trie()
trie.insert("apple")
trie.insert("app")
print(trie.search("apple"))  # Output: True
print(trie.search("app"))  # Output: True
print(trie.search("appl"))  # Output: False
print(trie.starts_with("ap"))  # Output: True
