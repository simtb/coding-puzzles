class Solution {
public:
    int findKthPositive(vector<int>& arr, int k) {
        int missing = 0;
        
        missing += (arr[0] - 1);
        if (k <= missing){
            return k;
        }
        
        int n = arr.size();
        
        for (int i = 1; i < n; i++){
            missing += (arr[i] - arr[i - 1] - 1);
            
            if (k <= missing){
                return arr[i] - (missing - k + 1);
            }
        }
        
        return arr[n - 1] + (k - missing);
    }
};