class Solution {
public:
    int getMaximumGenerated(int n) {
        if (n == 0){
            return 0;
        }
        
        if (n == 1 || n == 2){
            return 1;
        }
        
        int ans = 0;
        vector<int> dp(n + 1, 0);
        dp[1] = 1;
        int m = (n / 2) + 1;
        
        for (int i = 1; i < m; i++){
            if ((2 * i) + 1 > n){
                break;
            }
            
            dp[(2 * i)] = dp[i];
            ans = max(ans, dp[(2 * i)]);
            
            dp[(2 * i) + 1] = dp[i] + dp[i + 1];
            ans = max(ans, dp[(2 * i) + 1]);
        }
        
        return ans;
    }
};