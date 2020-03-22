"""
This problem was asked by Twitter.

A classroom consists of N students, whose friendships can be represented in an adjacency list. For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.

{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group. For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.

Given a friendship list such as the one above, determine the number of friend groups in the class.
"""

from typing import List


def friendships(classroom: dict) -> int:
    friendships: List[set] = []
    visited: dict = {}
    
    for person in classroom:
        if visited.get(person) == None:
            friendship: set = {person}
            visited[person]: bool = True
            queue: List[int] = classroom[person]
            while queue:
                current_person: int = queue.pop(0)
                for potential_friend in classroom[current_person]:
                    if visited.get(potential_friend) == None:
                        queue.append(potential_friend)
                friendship.add(current_person)
                if visited.get(current_person) == None:
                    visited[current_person]: bool = True
            friendships.append(friendship)
    return len(friendships)

