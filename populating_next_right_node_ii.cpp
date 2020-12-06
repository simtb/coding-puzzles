/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* left;
    Node* right;
    Node* next;

    Node() : val(0), left(NULL), right(NULL), next(NULL) {}

    Node(int _val) : val(_val), left(NULL), right(NULL), next(NULL) {}

    Node(int _val, Node* _left, Node* _right, Node* _next)
        : val(_val), left(_left), right(_right), next(_next) {}
};
*/

class Solution {
public:
    
    void helper(Node* root){
        deque<Node*> current_level;
        current_level.push_back(root);
        
        while (current_level.size() != 0){
            deque<Node*> next_level;
            
            while (current_level.size() > 0){
                Node* node = current_level.front();
                current_level.pop_front();
                
                if (node -> left){
                    next_level.push_back(node -> left);
                }
                
                if (node -> right){
                    next_level.push_back(node -> right);
                }
            }
            
            int m = next_level.size();
            
            if (m != 0){
                for (int i = 0; i < m - 1; i++){
                    Node* a = next_level[i];
                    Node* b = next_level[i + 1];
                    
                    a -> next = b;
                }
                
                next_level[m - 1] -> next = NULL;
                current_level = next_level;
            }
        }
    }
    
    
    Node* connect(Node* root) {
        if (!root){
            return root;
        }
        
        helper(root);
        return root;
    }
};
