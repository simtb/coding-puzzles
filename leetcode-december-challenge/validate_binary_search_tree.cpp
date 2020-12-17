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
    bool isValid = true;
    int current = INT_MIN;
    int i = 0;
    
    void helper(TreeNode* root){
        if (root && isValid){
            helper(root -> left);
            
            if (i == 0){
                i++;
                current = root -> val;
            }
            
            else{
                if (root -> val <= current){
                    isValid = false;
                }
                
                else{
                    current = root -> val;
                }
            }
            
            helper(root -> right);
        }
    }
    
    bool isValidBST(TreeNode* root) {
        helper(root);
        return isValid && isValid;
    }
};
