# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxDepth: int = -1
    paths: List[List[TreeNode]] = None
    
    def getMaxDepth(self, root: TreeNode, level: int) -> None:
        if root:
            self.maxDepth = max(self.maxDepth, level)
            self.getMaxDepth(root.left, level + 1)
            self.getMaxDepth(root.right, level + 1)
            
    def getPaths(self, root: TreeNode, level: int, path: tuple=()) -> None: 
        if root:
            tmp: List[TreeNode] = []
            for node in path:
                tmp.append(node)
            tmp.append(root)
            
            if level == self.maxDepth:
                self.paths.append(tmp)
            else:
                self.getPaths(root.left, level + 1, tuple(tmp))
                self.getPaths(root.right, level + 1, tuple(tmp))
                
                
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        
        self.getMaxDepth(root, 0)
            
        if self.paths is None:
            self.paths = []
            
        self.getPaths(root, 0)
        
        if len(self.paths) == 1:
            return self.paths[0][-1]
        
        n: int = len(self.paths)
        m: int = len(self.paths[0])
        ans: TreeNode = root
            
        for i in range(m):
            current: TreeNode = self.paths[0][m - 1 -i]
            same: bool = True
            for j in range(1, n):
                if self.paths[j][m - 1 - i].val == current.val:
                    pass
                else:
                    same = False
                    break
            if same:
                ans = current
                break
                    
        return ans
