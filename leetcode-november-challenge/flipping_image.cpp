class Solution {
public:
    vector<vector<int>> flipAndInvertImage(vector<vector<int>>& A) {
        int n = A.size();
        int m = A[0].size();
        
        for (int i = 0; i < n; i++){
            int left = 0;
            int right = m - 1;
            
            while (left <= right){
                int tmp_left = A[i][left];
                int tmp_right = A[i][right];
                A[i][left] = tmp_right;
                A[i][right] = tmp_left;
                
                if (left != right){
                    if (A[i][left] == 0){
                        A[i][left] = 1;
                    }
                    
                    else{
                        A[i][left] = 0;
                    }
                    
                    if (A[i][right] == 0){
                        A[i][right] = 1;
                    }
                    
                    else{
                        A[i][right] = 0;
                    }
                }
                
                else{
                    if (A[i][left] == 0){
                        A[i][left] = 1;
                    }
                    
                    else{
                        A[i][left] = 0;
                    }
                }
                left++;
                right--;
            }
        }
        return A;
    }
};
