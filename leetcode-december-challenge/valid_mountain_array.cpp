class Solution {
public:
    bool validMountainArray(vector<int>& arr) {
        int n = arr.size();
        
        if (n  < 3 || arr[0] > arr[1]){
            return false;
        }
        
        bool isMountain = true;
        bool increasing = true;
        
        for (int i = 1; i < n; i++){
            int current = arr[i];
            int prev = arr[i - 1];
            
            if (current == prev){
                isMountain = false;
                break;
            }
            
            else if (current < prev && increasing){
                increasing = false;
            }
            
            else if (current > prev && !increasing){
                isMountain = false;
                break;
            }
        }
        
        return isMountain && !increasing;
    }
};
