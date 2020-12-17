class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> ans(nums.size(), 0);
        int n = nums.size();
        int left = 0;
        int right = n - 1;
        
        for (int i = 0; i < n; i++){
            int a = abs(nums[left]);
            int b = abs(nums[right]);
            
            if (b >= a){
                ans[n - 1 - i] = b * b;
                right--;
            }
            
            else{
                ans[n - 1 - i] = a * a;
                left++;
            }
            
            
        }
        
        return ans;
    }
};
