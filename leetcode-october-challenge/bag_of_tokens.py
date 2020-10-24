"""
You have an initial power of P, an initial score of 0, and a bag of tokens where tokens[i] is the value of the ith token (0-indexed).

Your goal is to maximize your total score by potentially playing each token in one of two ways:

If your current power is at least tokens[i], you may play the ith token face up, losing tokens[i] power and gaining 1 score.
If your current score is at least 1, you may play the ith token face down, gaining tokens[i] power and losing 1 score.
Each token may be played at most once and in any order. You do not have to play all the tokens.

Return the largest possible score you can achieve after playing any number of tokens.
"""

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        tokens.sort()
        n: int = len(tokens)
        maxPoints: int = 0
        points: int = 0
        i: int = 0
        j: int = n - 1
        
        while (i <= j):
            if P >= tokens[i]:
                points += 1
                P -= tokens[i]
                i += 1
                maxPoints = max(maxPoints, points)
            elif points > 0:
                points -= 1
                P += tokens[j]
                j -= 1
            else:
                return maxPoints
        return maxPoints
