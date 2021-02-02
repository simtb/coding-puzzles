class Solution {
public:
    int getDistance(vector<int> A, vector<int> B){
        int dy = abs(A[0] - B[0]);
        int dx = abs(A[1] - B[1]);
        
        return dx + dy;
    }
    
    
    int minDistance(int height, int width, vector<int>& tree, vector<int>& squirrel, vector<vector<int>>& nuts) {
        int ans = 0;
        vector<int> start_nut = nuts[0];
        int a = getDistance(tree, nuts[0]);
        int b = getDistance(squirrel, nuts[0]);
        int saving = b - a;
        int index = 0;
        int n = nuts.size();
        
        for (int i = 1; i < n; i++){
            vector<int> nut = nuts[i];
            int x = getDistance(tree, nut);
            int y = getDistance(squirrel, nut);
            int s = y - x;
            
            if (s < saving){
                start_nut = nut;
                saving = s;
                index = i;
            }
        }
        
        for (int i = 0; i < n; i++){
            if (i != index){
                int tmp = getDistance(tree, nuts[i]);
                ans += (2 * tmp);
            }
        }
        
        ans += getDistance(squirrel, start_nut);
        ans += getDistance(start_nut, tree);
        
        
        return ans;
    }
};