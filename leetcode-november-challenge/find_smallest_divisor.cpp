class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        int n = nums.size();
        int left = 1;
        int right = nums[n - 1];
        
        
        int ans = right;
        
        while (left <= right){
            int mid = (left + right) / 2;
            
            vector<int> tmp(n);
            int total = 0;
            
            for (int i = 0; i < n; i++){
                int current = nums[i];
                
                if (current % mid == 0){
                    tmp[i] = current / mid;
                }
                
                else{
                    tmp[i] = (current / mid) + 1;
                }
                
                total += tmp[i];
            }
            
            if (total > threshold){
                left = mid + 1;
            }
            
            else{
                ans = mid;
                right = mid - 1;
            }
            
        }
        
        return ans;
    }
};
