class Solution {
public:
    int maxOperations(vector<int>& nums, int k) {
        int ans = 0;
        unordered_map<int, int> seen;
        
        for (int num: nums){
            if (seen.find(k - num) != seen.end() && seen[k - num] > 0){
                ans++;
                seen[k - num]--;
            }
            
            else{
                if (seen.find(num) == seen.end()){
                    seen[num] = 1;
                }
                
                else{
                    seen[num]++;
                }
            }
        }
        return ans;
    }
};