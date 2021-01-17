class Solution {
public:
    int countVowelStrings(int n) {
        int last_total = 0;
        vector<vector<int>> dp(n, vector(5, 0));
        
        for (int i = 0; i < n; i++){
            int c = 0;
            for (int j = 0; j < 5; j++){
                if (i == 0){
                    dp[i][j] = 1;
                    c++;
                }
                
                else{
                    if (j == 0){
                        dp[i][j] = last_total;
                        c += last_total;
                    }
                    
                    else{
                        int tmp = last_total;
                        for (int k = 0; k < j; k++){
                            tmp -= dp[i - 1][k];
                        }
                        
                        dp[i][j] = tmp;
                        c += tmp;
                    }
                }
            }
            
            last_total = c;
        }
        return last_total;
    }
};