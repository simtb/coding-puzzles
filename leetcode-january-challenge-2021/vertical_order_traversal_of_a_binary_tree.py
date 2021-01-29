# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        x_coordinates: dict = dict()
        tmp: List[int] = []
        
        queue: deque = deque()
        queue.appendleft((root, 0, 0))
        
        while (queue):
            element: tuple = queue.pop()
            current_node: TreeNode = element[0]
            current_value: int = current_node.val
            current_x: int = element[1]
            current_y: int = element[2]
            
            if current_x not in x_coordinates:
                x_coordinates[current_x]: List[tuple] = [(current_value, current_y)]
                tmp.append(current_x)
            else:
                x_coordinates[current_x].append((current_value, current_y))
            
            if current_node.left:
                queue.appendleft((current_node.left, current_x - 1, current_y - 1))
            if current_node.right:
                queue.appendleft((current_node.right, current_x + 1, current_y - 1))
                
        ans: List[List[int]] = []
        tmp.sort()
        
        for num in tmp:
            a: List[int] = []
            x_coordinates[num].sort(key=lambda x: (-x[1], x[0]))
            for b in x_coordinates[num]:
                a.append(b[0])
            ans.append(a)
            
        return ans