class Solution {
public:
    int numDecodings(string s) {
        int n = s.size();
        
        if (n == 0){
            return 0;
        }
        
        vector<int> dp(n + 1, 0);
        
        dp[0] = 1;
        
        if (s[0] != '0'){
            dp[1] = 1;
        }
        
        else{
            dp[1] = 0;
        }
        
        for (int i = 2; i < n + 1; i++){
            if (s[i - 1] != '0'){
                dp[i] += dp[i - 1];
            }
            
            string tmp = "";
            tmp += s[i - 2];
            tmp += s[i - 1];
            
            if (10 <= stoi(tmp) && stoi(tmp) <= 26){
                dp[i] += dp[i - 2];
            }
        }
        return dp[n];
    }
};