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
    ListNode* deleteDuplicates(ListNode* head) {
        if (!head){
            return head;
        }
        
        ListNode* dummyHead = new ListNode(0);
        ListNode* tmp = dummyHead;
        ListNode* previous_node = head;
        int count = 1;
        ListNode* current_node = head -> next;
        
        while (current_node){
            if (previous_node -> val == current_node -> val){
                count++;
            }
            
            else{
                if (count == 1){
                    previous_node -> next = NULL;
                    tmp -> next = previous_node;
                    tmp = tmp -> next;
                    previous_node = current_node;
                }
                
                else{
                    count = 1;
                    previous_node = current_node;
                }
            }
            
            current_node = current_node -> next;
        }
        
        if (count == 1){
            tmp -> next = previous_node;
        }
        
        return dummyHead -> next;
    }
};