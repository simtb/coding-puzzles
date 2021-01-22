class Solution {
public:
    bool closeStrings(string word1, string word2) {
        int n = word1.size();
        int m = word2.size();
        
        if (n != m){
            return false;
        }
        
        unordered_map<char, int> c1;
        unordered_map<char, int> c2;
        
        for (auto _: word1){
            if (c1.find(_) != c1.end()){
                c1[_]++;
            }
            
            else{
                c1[_] = 1;
            }
        }
        
        
        for (auto _: word2){
            if (c1.find(_) == c1.end()){
                return false;
            }
            
            else{
                if (c2.find(_) != c2.end()){
                    c2[_]++;
                }
                
                else{
                    c2[_] = 1;
                }
            }
        }
        
        if (c1.size() != c2.size()){
            return false;
        }
        
        vector<int> f1;
        vector<int> f2;
        
        for (auto element: c1){
            f1.push_back(element.second);
        }
        
        for (auto element: c2){
            f2.push_back(element.second);
        }
        
        sort(f1.begin(), f1.end());
        sort(f2.begin(), f2.end());
        
        bool ans = true;
        int x = f1.size();
        
        for(int i = 0; i < x; i++){
            if (f1[i] != f2[i]){
                ans = false;
                break;
            }
        }
        
        return ans;
    }
};