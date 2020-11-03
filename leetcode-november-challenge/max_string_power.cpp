class Solution {
public:
    int maxPower(string s) {
        int n = s.size();
        char current = s[0];
        int tmp = 1;
        int ans = 1;
        
        for (int i = 1; i < n; i++){
            char letter = s[i];
            
            if (current == letter){
                tmp++;
            }
            
            else{
                ans = max(ans, tmp);
                current = letter;
                tmp = 1;
            }
        }
        return max(ans, tmp);
    }
};
