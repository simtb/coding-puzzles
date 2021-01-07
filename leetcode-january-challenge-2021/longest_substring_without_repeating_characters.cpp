class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.size();
        int ans = 0;
        int i = 0;
        int j = 0;
        unordered_map<char,int> seen;
        
        while (i < n && j < n){
            char current = s[j];
            
            if (seen.find(current) != seen.end()){
                i = max(seen[current], i);
            }
            
            ans = max(ans, j - i + 1);
            seen[current] = j + 1;
            j++;
        }
        return ans;
    }
};