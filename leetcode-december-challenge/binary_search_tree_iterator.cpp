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
class BSTIterator {
public:
    int pointer = -1;
    vector<int> t;
    void helper(TreeNode* root){
        if (root){
            helper(root -> left);
            t.push_back(root -> val);
            helper(root -> right);
        }
    }
    BSTIterator(TreeNode* root) {
        helper(root);
    }
    
    int next() {
        pointer++;
        return t[pointer];
    }
    
    bool hasNext() {
        return pointer + 1 < t.size();
    }
};

/**
 * Your BSTIterator object will be instantiated and called as such:
 * BSTIterator* obj = new BSTIterator(root);
 * int param_1 = obj->next();
 * bool param_2 = obj->hasNext();
 */
