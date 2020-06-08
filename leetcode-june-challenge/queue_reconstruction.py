"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.
"""

class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # 1. Descending order by height 
        # 2. same hight ascending order by the number of people in front 
        people.sort(key=lambda p:(-p[0], p[1]))
        print(people)
        re_people = []
        
        # Insert into the corresponding position according to the number of people in front
        for p in people:
            re_people.insert(p[1], p)
            
        return re_people
