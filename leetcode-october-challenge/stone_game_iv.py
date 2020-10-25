"""
Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile.  On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n. Return True if and only if Alice wins the game otherwise return False, assuming both players play optimally.
"""

class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        can_win: bool = [False] * (n + 1)
        
        for i in range(1, n + 1):
            possible: bool = True
            for j in range(1, i + 1):
                square: int = j * j
                if square > i:
                    break
                if not can_win[i - square]:
                    possible = False
                    break
                    
            can_win[i] = not possible
            
        return can_win[n]
            
