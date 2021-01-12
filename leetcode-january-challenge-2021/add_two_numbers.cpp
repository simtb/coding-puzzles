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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* dummyHead = new ListNode(0);
        ListNode* current = dummyHead;
        ListNode* pointerA = l1;
        ListNode* pointerB = l2;
        ListNode* new_node;
        int carry = 0;
        int new_value;
        
        while (pointerA && pointerB){
            new_value = pointerA -> val + pointerB -> val + carry;
            carry = new_value / 10;
            new_node = new ListNode(new_value % 10);
            current -> next = new_node;
            current = current -> next;
            pointerA = pointerA -> next;
            pointerB = pointerB -> next;
        }
        
        if (pointerA){
            while (pointerA){
                new_value = pointerA -> val + carry;
                carry = new_value / 10;
                new_node = new ListNode(new_value % 10);
                current -> next = new_node;
                current = current -> next;
                pointerA = pointerA -> next;
            }
        }
        
        if (pointerB){
            while (pointerB){
                new_value = pointerB -> val + carry;
                carry = new_value / 10;
                new_node = new ListNode(new_value % 10);
                current -> next = new_node;
                current = current -> next;
                pointerB = pointerB -> next;
            }
        }
        
        if (carry){
            current -> next = new ListNode(1);
        }
        
        return dummyHead -> next;
    }
};