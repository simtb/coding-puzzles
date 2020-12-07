class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> ans(n, vector<int>(n, 0));
        
        int x = 0;
        int end = n * n;
        
        int right_start = 0;
        int right_end = n;
        int right_row = 0;
        
        int down_start = 1;
        int down_end = n;
        int down_column = n - 1;
        
        int left_start = n - 2;
        int left_end = -1;
        int left_row = n - 1;
        
        int up_start = n - 2;
        int up_end = 0;
        int up_column = 0;
        
        while (true){
            for (int a = right_start; a < right_end; a++){
                x++;
                ans[right_row][a] = x;
            }
            
            if (x == end){
                break;
            }
            
            right_start++;
            right_end--;
            right_row++;
            
            for (int b = down_start; b < down_end; b++){
                x++;
                ans[b][down_column] = x;
            }
            
            if (x == end){
                break;
            }
            
            down_start++;
            down_end--;
            down_column--;
            
            for (int c = left_start; c > left_end; c--){
                x++;
                ans[left_row][c] = x;
            }
            
            if (x == end){
                break;
            }
            
            left_start--;
            left_end++;
            left_row--;
            
            for (int d = up_start; d > up_end; d--){
                x++;
                ans[d][up_column] = x;
            } 
            
            if (x == end){
                break;
            }
            
            up_start--;
            up_end++;
            up_column++;
        }
        
        return ans;
    }
};
