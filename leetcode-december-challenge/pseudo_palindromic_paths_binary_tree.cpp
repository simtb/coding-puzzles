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
    
    bool isPalindrome(string S){
        unordered_map<char, int> tmp;
        for (char s: S){
            if (tmp.find(s) == tmp.end()){
                tmp[s] = 1;
            }
            
            else{
                tmp[s]++;
            }
        }
        
        int number_of_odd = 0;
        
        for (auto element: tmp){
            if (element.second % 2 == 1){
                number_of_odd++;
            }
            
            if (number_of_odd > 1){
                return false;
            }
        }
        
        return true;
    }
    
    void preOrder(TreeNode* root, string path){
        if (root){
            path += to_string(root -> val);
            if (!root -> left && !root -> right){
                if (isPalindrome(path)){
                    ans++;
                }
            }
            
            preOrder(root -> left, path);
            preOrder(root-> right, path);
        }
    }
    int pseudoPalindromicPaths (TreeNode* root) {
        preOrder(root, "");
        return ans;
    }
}; 