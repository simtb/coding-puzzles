class Solution {
public:
    bool kLengthApart(vector<int>& nums, int k) {
        bool ans = true;
        int n = nums.size();
        int last = -1;
        
        for (int i = 0; i < n; i++){
            if (nums[i] == 1){
                if (last == -1){
                    last = i;
                }
                
                else{
                    if (i - last >= k + 1){
                        last = i;
                    }
                    
                    else{
                        ans = false;
                        break;
                    }
                }
            }
            
            else{
                ;
            }
        }
        
        return ans;
    }
};