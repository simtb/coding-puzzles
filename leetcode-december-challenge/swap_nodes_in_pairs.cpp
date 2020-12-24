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
    ListNode* swapPairs(ListNode* head) {
        if (!head){
            return head;
        }
        
        int i = 0;
        ListNode* new_head;
        
        ListNode* current = head;
        ListNode* previous;
        
        while (current){
            if (i == 0){
                if (current -> next){
                    ListNode* tmp = current -> next -> next;
                    ListNode* next_node = current -> next;
                    current -> next = NULL;
                    next_node -> next = NULL;
                    next_node -> next = current;
                    current -> next = tmp;
                    new_head = next_node;
                    current = next_node;
                }
                
                else{
                    new_head = current;
                }
            }
            
            else if (i % 2 == 0){
                if (current-> next){
                    ListNode* tmp = current -> next -> next;
                    ListNode* next_node = current -> next;
                    current -> next = NULL;
                    next_node -> next = NULL;
                    previous -> next = next_node;
                    next_node -> next = current;
                    current -> next = tmp;
                    current = next_node;
                }
            }
            
            else{
                previous = current;
            }
            
            i++;
            current = current -> next;
        }
        return new_head;
        
    }
};