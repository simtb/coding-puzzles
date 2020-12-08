class Solution {
public:
    vector<string> findMissingRanges(vector<int>& nums, int lower, int upper) {
        if (nums.size() == 0){
            if (lower == upper){
                return {to_string(upper)};
            }
            
            else{
                return {to_string(lower) + "->" + to_string(upper)};
            }
        }
        
        if (lower == upper){
            if (nums.size() == 0){
                return {to_string(lower)};
            }
            
            else{
                return {};
            }
        }
        
        vector<string> ans;
        int m = nums.size();
        
        if (lower < nums[0]){
            if (nums[0] - lower == 1){
                ans.push_back(to_string(lower));
            }
            
            else{
                ans.push_back(to_string(lower) + "->" + to_string(nums[0] - 1));
            }
        }
        for (int i = 0; i < m - 1; i++){
            if (nums[i + 1] - nums[i] == 1){
                ;
            }
            
            else if (nums[i + 1] - nums[i] == 2){
                ans.push_back(to_string(nums[i] + 1));
            }
            
            else{
                ans.push_back(to_string(nums[i] + 1) + "->" + to_string(nums[i + 1] - 1));
            }
        }
        
        if (upper == nums[m - 1]){
            ;
        }
        
        else{
            if (upper - nums[m - 1] == 1){
                ans.push_back(to_string(upper));
            }
            
            else{
                ans.push_back(to_string(nums[m - 1] + 1) + "->" + to_string(upper));
            }
        }
        
        
        return ans;
    }
};
