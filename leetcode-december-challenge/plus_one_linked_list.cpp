/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* plusOne(ListNode* head) {
        stack<ListNode*> tmp;
        ListNode* current = head;
        
        while (current){
            tmp.push(current);
            current = current -> next;
        }
        
        int n = tmp.size();
        bool carry_over = false;
        
        for (int i = 0; i < n; i++){
            ListNode* node = tmp.top();
            int value = node -> val;
            tmp.pop();
            
            if (i == 0){
                int new_value = value + 1;
                if (new_value == 10){
                    carry_over = true;
                    node -> val = new_value % 10;
                }
                
                else{
                    node -> val = new_value;
                    break;
                }
            }
            
            else{
                if (!carry_over){
                    break;
                }
                
                else{
                    int new_value = value + 1;
                    if (new_value == 10){
                        node -> val = new_value % 10;
                    }
                    
                    else{
                        carry_over = false;
                        node -> val = new_value;
                        break;
                    }
                }
            }
        }
        
        
        if (!carry_over){
            return head;
        }
        
        else{
            ListNode* new_head = new ListNode(1);
            new_head -> next = head;
            return new_head;
        }

    }
};
