class Solution {
public:
    int ans = 0;
    
    void helper(int n, int current_position, vector<bool> visited){
        if (current_position > n){
            ans++;
        }
        
        for (int i = 1; i < n + 1; i++){
            if (!visited[i] && (i % current_position == 0 || current_position % i == 0)){
                visited[i] = true;
                helper(n, current_position + 1, visited);
                visited[i] = false;
            }
        }
    }
    
    int countArrangement(int n) {
        vector<bool> visited(n + 1, false);
        helper(n, 1, visited);
        return ans;
    }
};