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
    TreeNode* findNearestRightNode(TreeNode* root, TreeNode* u) {
        deque<deque<TreeNode*>> q;
        deque<TreeNode*> start;
        start.push_back(root);
        q.push_back(start);
        
        while (q.size() > 0){
            deque<TreeNode*> current_level = q.front();
            q.pop_front();
            deque<TreeNode*> next_level;
            bool found = false;
            
            while(current_level.size() > 0){
                TreeNode* node = current_level.front();
                current_level.pop_front();
                
                if (node -> left){
                    if (found){
                        return node -> left;
                    }
                    
                    if (node -> left -> val == u -> val){
                        found = true;
                    }
                    next_level.push_back(node -> left);
                }
                
                if (node -> right){
                    if (found){
                        return node -> right;
                    }
                    
                    if (node -> right -> val == u -> val){
                        found = true;
                    }
                    next_level.push_back(node -> right);
                }
            }