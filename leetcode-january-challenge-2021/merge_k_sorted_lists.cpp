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
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        vector<int> tmp;
        
        for (auto l: lists){
            while (l){
                tmp.push_back(l -> val);
                l = l -> next;
            }
        }
        
        if (tmp.size() == 0){
            return NULL;
        }
        
        sort(tmp.begin(), tmp.end());
        ListNode* head = new ListNode(tmp[0]);
        ListNode* current = head;
        int m = tmp.size();
        
        for (int i = 1; i < m; i++){
            ListNode* node = new ListNode(tmp[i]);
            current -> next = node;
            current = current -> next;
        }
        
        return head;
    }
};