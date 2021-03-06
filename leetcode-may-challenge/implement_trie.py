"""
Implement a trie with insert, search, and startsWith methods.
"""

class TreeNode:
    def __init__(self, v: str):
        self.v: str = v
        self.children: dict = {}
        self.end_here: bool = False
        

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root: TreeNode = TreeNode(None)
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        parent: TreeNode = self.root
        
        for i, char in enumerate(word):
            if char not in parent.children:
                parent.children[char]: TreeNode = TreeNode(char)
            parent = parent.children[char]
            
            if i == len(word) - 1:
                parent.end_here: bool = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        
        parent: TreeNode = self.root
        
        for char in word:
            if char not in parent.children:
                return False
            parent: TreeNode = parent.children[char]
        return parent.end_here
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        
        parent: TreeNode = self.root
        
        for char in prefix:
            if char not in parent.children:
                return False
            parent: TreeNode = parent.children[char]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
