class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int max_area = 0;
        stack<vector<int>> s;
        int n = heights.size();
        
        for (int i = 0; i < n; i++){
            int start = i;
            int current_height = heights[i];
            
            while (s.size() != 0 && s.top()[1] > current_height){
                vector<int> tmp = s.top();
                int index = tmp[0];
                int old_max_height = tmp[1];
                max_area = max(max_area, old_max_height * (i - index));
                start = index;
                s.pop();
            }
            
            s.push({start, current_height});
        }
        
        while (s.size() != 0){
            vector<int> a = s.top();
            int j = a[0];
            int h = a[1];
            
            max_area = max(max_area, h * (n - j));
            s.pop();
        }
        return max_area;
    }
};