"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n: int = len(board)
        m: int = len(board[0])
        first_character: str = word[0]
        
        for i in range(n):
            for j in range(m):
                current: str = board[i][j]
                if current == first_character and self.dfs(i, j, word, 0, board):
                    return True
        return False
    
    
    def dfs(self, i: int, j: int, word: str, length: int, board: List[List[str]]) -> bool:
        if len(word) == length:
            return True
        if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[length]:
            return False
        
        tmp: str = board[i][j]
        board[i][j] = ''
        
        found: bool = self.dfs(i + 1, j, word, length + 1, board) or self.dfs(i - 1, j, word, length + 1, board) or self.dfs(i, j + 1, word, length + 1, board,) or self.dfs(i, j - 1, word, length + 1, board)
        
        board[i][j] = tmp
        
        return found
