class Solution {
public:
    string longestPalindrome(string s) {
        if (s.size() < 1){
            return "";
        }
        
        int start = 0;
        int end = 0;
        
        for (int i=0; i < s.size(); i++){
            int a = helper(s, i, i);
            int b = helper(s, i, i + 1);
            int c = max(a, b);
            
            if (c > end - start){
                start = i - ((c - 1) / 2);
                end = i + (c / 2);
            }
        }
        
        return s.substr(start, end - start + 1);
    }
private:
    int helper(string s, int left, int right){
        while (0 <= left && right < s.size() && s[left] == s[right]){
            left--;
            right++;
        }
        
        return right - left - 1;
    }
};