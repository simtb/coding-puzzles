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
    bool isBalanced(TreeNode* root) {
        int height;
        return isBalancedTreeHelper(root, height);
    }
private:
    bool isBalancedTreeHelper(TreeNode* root, int& height){
        if (!root){
            height = -1;
            return true;
        }
        
        int left;
        int right;
        
        if (isBalancedTreeHelper(root -> left, left) && isBalancedTreeHelper(root -> right, right) && abs(left - right) <2){
            height = 1 + max(left, right);
            return true;
        }
        
        else{
            return false;
        }
    }
};