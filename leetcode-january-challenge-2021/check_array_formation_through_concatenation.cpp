class Solution {
public:
    bool canFormArray(vector<int>& arr, vector<vector<int>>& pieces) {
        unordered_map<int, vector<int>> tmp;
        
        for (auto piece: pieces){
            tmp[piece[0]] = piece;
        }
        
        int n = arr.size();
        int i = 0;
        
        while (i < n){
            int current = arr[i];
            
            if (tmp.find(current) == tmp.end()){
                return false;
            }
            
            vector<int> current_piece = tmp[current];
            
            for (auto num: current_piece){
                if (num != arr[i]){
                    return false;
                }
                
                i++;
            }
        }
        return true;
    }
};