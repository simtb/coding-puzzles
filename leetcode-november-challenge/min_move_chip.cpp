class Solution {
public:
    int minCostToMoveChips(vector<int>& position) {
        int evens = 0;
        int odds = 0;
        
        for (auto p: position){
            if (p % 2 == 0){
                evens++;
            }
            
            else{
                odds++;
            }
        }
        
        return min(odds, evens);
    }
};
