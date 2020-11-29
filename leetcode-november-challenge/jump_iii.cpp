class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        int n = arr.size();
        unordered_set<int> seen;
        vector<int> queue = {start};
        
        while (!queue.empty()){
            int current_position = queue.back();
            queue.pop_back();
            
            int jump = arr[current_position];
            
            if (jump == 0){
                return true;
            }
            
            int a = current_position + jump;
            int b = current_position - jump;
            
            if (0 <= a && a < n && seen.find(a) == seen.end()){
                seen.insert(a);
                queue.push_back(a);
            }
            
            if (0 <= b && b < n && seen.find(b) == seen.end()){
                seen.insert(b);
                queue.push_back(b);
            }
        }
        return false;
        
    }
};
