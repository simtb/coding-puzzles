class Solution {
public:
    int countCornerRectangles(vector<vector<int>>& grid) {
        int ans = 0;
        int m = grid[0].size();
        unordered_map<string, int> counter;
        
        for (vector<int> row: grid){
            for (int i = 0; i < m; i++){
                if (row[i]){
                    for (int j = i + 1; j < m; j++){
                        if (row[j]){
                            string tmp = "";
                            string string_i = to_string(i);
                            string string_j = to_string(j);
                            tmp += string_i;
                            tmp += ' ';
                            tmp += string_j;
                            
                            if (counter.find(tmp) == counter.end()){
                                counter[tmp] = 0;
                            }
                            
                            ans += counter[tmp];
                            counter[tmp] += 1;
                        }
                    }
                }
            }
        }
        
        return ans;
    }
};