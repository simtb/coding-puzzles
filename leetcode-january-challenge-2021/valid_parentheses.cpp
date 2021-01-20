class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> mapping;
        mapping[')'] = '(';
        mapping[']'] = '[';
        mapping['}'] = '{';
        unordered_set<char> o;
        o.insert('(');
        o.insert('[');
        o.insert('{');
        
        stack<char> a;
        
        for (char x: s){
            if (o.find(x) != o.end()){
                a.push(x);
            }
            
            else{
                if (a.size()){
                    char y = a.top();
                    if (mapping[x] == y){
                        ;
                    }
                    
                    else{
                        return false;
                    }
                    
                    a.pop();
                }
                
                else{
                    return false;
                }
            }
        }