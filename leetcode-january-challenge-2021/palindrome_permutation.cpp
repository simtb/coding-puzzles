class Solution {
public:
    bool canPermutePalindrome(string s) {
        bool ans = true;
        unordered_map<char, int> counter;
        
        for (auto c: s){
            if (counter.find(c) == counter.end()){
                counter[c] = 1;
            }
            
            else{
                counter[c]++;
            }
        }
        
        int odd = 0;
        
        for (auto element: counter){
            if (element.second % 2 == 1){
                odd++;
            }
            
            if (odd > 1){
                ans = false;
                break;
            }
        }
        return ans;
    }
};