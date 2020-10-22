"""
We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
"""

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack: List[int] = []
        
        for asteroid in asteroids:
            if asteroid > 0 or not stack:
                stack.append(asteroid)
            else:
                if stack[-1] < 0:
                    stack.append(asteroid)
                else:
                    while (stack):
                        if stack[-1] > 0:
                            if abs(stack[-1]) > abs(asteroid):
                                break
                            if abs(stack[-1]) == abs(asteroid):
                                stack.pop()
                                break
                            if abs(asteroid) > abs(stack[-1]):
                                stack.pop()
                                if not stack:
                                    stack.append(asteroid)
                                    break
                        else:
                            stack.append(asteroid)
                            break
        return stack
