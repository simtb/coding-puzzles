class Solution {
public:
    void gameOfLife(vector<vector<int>>& board) {
        unordered_map<int, int> tmp;
        int m = board.size();
        int n = board[0].size();
        vector<vector<int>> directions = {{1, 1}, {1, -1}, {-1, 1}, {-1, -1}, {0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                queue<vector<int>> q;
                for (auto direction: directions){
                    int new_y = i + direction[0];
                    int new_x = j + direction[1];
                    if (0 <= new_y && 0 <= new_x && new_y < m && new_x < n){
                        vector<int> a = {new_y, new_x};
                        q.push(a);
                    }
                }
                
                int live = 0;
                
                while (q.size() != 0){
                    vector<int> neighbour = q.front();
                    q.pop();
                    if (board[neighbour[0]][neighbour[1]] == 1){
                        live++;
                    }
                }
                
                int key = (n * i) + j;
                
                if (board[i][j] == 1 && live < 2){
                    tmp[key] = 0;
                }
                
                else if (board[i][j] == 1 && (live == 2 || live == 3)){
                    tmp[key] = 1;
                }
                
                else if (board[i][j] == 1 && live > 3){
                    tmp[key] = 0;
                }
                
                else if (board[i][j] == 0 && live == 3){
                    tmp[key] = 1;
                }
            }
        }
        
        
        for (auto key: tmp){
            int a = key.first / n;
            int b = key.first % n;
            
            board[a][b] = key.second;
        }
    }
};