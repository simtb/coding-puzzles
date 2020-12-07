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
    vector<TreeNode*> order;
    
    
    void inOrder(TreeNode* root){
        if (root){
            inOrder(root -> left);
            order.push_back(root);
            inOrder(root -> right);
        }
    }
    
    
    TreeNode* increasingBST(TreeNode* root) {
        if (!root){
            return root;
        }
        
        inOrder(root);
        
        int n = order.size();
        
        for (int i = 0; i < n - 1; i++){
            order[i] -> left = NULL;
            order[i] -> right = order[i + 1]; 
        }
        
        order[n - 1] -> left = NULL;
        
        return order[0];
    }
};
