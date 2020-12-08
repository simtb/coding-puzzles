class Solution {
public:
    int numPairsDivisibleBy60(vector<int>& time) {
        unordered_map<int, int> counter;
        int ans = 0;
        
        for (auto t: time){
            int needed;
            if (t % 60 == 0){
                needed = 0;
            }
            
            else{
                needed = 60 - (t % 60);
            }
            
            if (counter.find(needed) != counter.end()){
                ans += counter[needed];
            }
            
            if (counter.find(t % 60) != counter.end()){
                counter[t % 60]++;
            }
            
            else{
                counter[t % 60] = 1;
            }
        }
        
        return ans;
    }
};
