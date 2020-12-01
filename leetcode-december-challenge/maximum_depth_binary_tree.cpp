/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans = 0;
    
    void helper(TreeNode* root, int level){
        if (root){
            level++;
            ans = max(ans, level);
            helper(root -> left, level);
            helper(root -> right, level);
        }
    }
    
    
    int maxDepth(TreeNode* root) {
        if (!root){
            return 0;
        }
        
        helper(root, 0);
        
        return ans;
    }
};
