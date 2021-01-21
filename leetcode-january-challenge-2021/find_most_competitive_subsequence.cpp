class Solution {
public:
    vector<int> mostCompetitive(vector<int>& nums, int k) {
        vector<int> s;
        int n = nums.size();
        vector<int> ans;
        
        for (int i = 0; i < n; i++){
            int num = nums[i];
            int min_stack_length = max(0, k - n + i);
            
            while (s.size() > min_stack_length && num < s.back()){
                s.pop_back();
            }
            
            s.push_back(num);
        }
        
        for (int j = 0; j < k; j++){
            ans.push_back(s[j]);
        }
        
        return ans;
    }
};