"""

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    tmp: List[TreeNode] = None
    
    
    def inOrder(self, root: TreeNode) -> None:
        if root:
            self.inOrder(root.left)
            self.tmp.append(root)
            self.inOrder(root.right)
    
    
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        if self.tmp is None:
            self.tmp = []
        
        self.inOrder(root)
        
        order: List[int] = []
        
        n: int = len(self.tmp)
        
        for i in range(n):
            order.append(self.tmp[i].val)
        
        correct_order = sorted(order)
        
        a: int = None
        b: int = None
        
        for i in range(n):
            if correct_order[i] != order[i]:
                if a is None:
                    a = i
                else:
                    b = i
                    break
        
        self.tmp[a].val, self.tmp[b].val = self.tmp[b].val, self.tmp[a].val
