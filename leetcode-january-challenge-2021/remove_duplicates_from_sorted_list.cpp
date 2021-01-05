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
        int current_value = head -> val;
        int count = 1;
        ListNode* current_node = head -> next;
        
        while (current_node){
            if (current_value == current_node -> val){
                count++;
            }
            
            else{
                if (count == 1){
                    tmp -> next = new ListNode(current_value);
                    tmp = tmp -> next;
                    current_value = current_node -> val;
                }
                
                else{
                    count = 1;
                    current_value = current_node -> val;
                }
            }
            current_node = current_node -> next;
        }
        
        if (count == 1){
            tmp -> next = new ListNode(current_value);
        }
        return dummyHead -> next;
    }
};