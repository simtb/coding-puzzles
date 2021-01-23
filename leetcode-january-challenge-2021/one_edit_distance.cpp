class Solution {
public:
    bool isOneEditDistance(string s, string t) {
        int n = s.size();
        int m = t.size();
        
        if (abs(n - m) > 1){
            return false;
        }
        
        if (n == m){
            int a = 0;
            int diff = 0;
            
            while (a < n){
                if (s[a] != t[a]){
                    diff++;
                }
                
                if (diff > 1){
                    break;
                }
                
                a++;
            }
            
            if (diff != 1){
                return false;
            }
        }
        
        else{
            int x = 0;
            int y = 0;
            int diff = 0;
            
            while (x < n && y < m){
                if (s[x] != t[y]){
                    diff++;
                    if (n > m){
                        x++;
                    }
                    
                    else if (m > n){
                        y++;
                    }
                }
                
                else{
                    x++;
                    y++;
                }
                
                if (diff > 1){
                    break;
                }
            }
            
            if (diff > 1){
                return false;
            }
        }
        
        return true;
    }
};