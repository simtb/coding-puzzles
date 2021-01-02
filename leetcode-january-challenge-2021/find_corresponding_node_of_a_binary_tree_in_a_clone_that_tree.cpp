/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* ans;
    void preOrder(TreeNode* root, TreeNode* target){
        if (root){
            if (root -> val == target -> val){
                ans = root;
            }
            
            preOrder(root -> left, target);
            preOrder(root -> right, target);
        }
    }
    TreeNode* getTargetCopy(TreeNode* original, TreeNode* cloned, TreeNode* target) {
        preOrder(cloned, target);
        return ans;
    }
};