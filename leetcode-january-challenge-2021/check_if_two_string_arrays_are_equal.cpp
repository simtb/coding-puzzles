class Solution {
public:
    bool arrayStringsAreEqual(vector<string>& word1, vector<string>& word2) {
        string a;
        string b;
        
        for (string x: word1){
            a += x;
        }
        
        for (string y: word2){
            b += y;
        }
        
        return a == b;
    }
};