class Solution {
public:
    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        int n = mat.size();
        int m = mat[0].size();
        
        if (n == 1){
            return mat;
        }
        
        int y = n - 1;
        
        while (0 <= y){
            vector<int> tmp;
            int i = y;
            int j = 0;
            
            while (0 <= i && i < n && 0 <= j && j < m){
                tmp.push_back(mat[i][j]);
                i++;
                j++;
            }
            
            sort(tmp.begin(), tmp.end());
            
            i = y;
            j = 0;
            
            for (int t: tmp){
                mat[i][j] = t;
                i++;
                j++;
            }
            
            y--;
        }
        
        int x = 1;
        
        while (x < m){
            vector<int> tmp;
            int i = 0;
            int j = x;
            
            while (0 <= i && i < n && 0 <= j && j < m){
                tmp.push_back(mat[i][j]);
                i++;
                j++;
            }
            
            sort(tmp.begin(), tmp.end());
            
            i = 0;
            j = x; 
            
            for (int t: tmp){
                mat[i][j] = t;
                i++;
                j++;
            }
            
            x++;
        }
        
        return mat;
        
    }
};