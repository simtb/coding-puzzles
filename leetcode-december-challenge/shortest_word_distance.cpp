class Solution {
public:
    int shortestDistance(vector<string>& words, string word1, string word2) {
        int n = words.size();
        int a = -1;
        int b = -1;
        
        int ans = INT_MAX;
        
        for (int i = 0; i < n; i++){
            string current = words[i];
            
            if (current == word1){
                a = i;
            }
            
            if (current == word2){
                b = i;
            }
            
            if (a >= 0 && b >= 0){
                ans = min(ans, abs(a -b ));
            }
            
        }
        return ans;
    }
};
