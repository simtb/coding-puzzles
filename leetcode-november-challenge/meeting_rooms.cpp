bool f(vector<int> a, vector<int> b){
    if (a[0] < b[0]){
        return true;
    }
    else{
        return false;
    }
}




class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        int n = intervals.size();
        
        if (n < 2){
            return true;
        }
        
        sort(intervals.begin(), intervals.end(), f);
        vector<int> current_meeting = intervals[0];
        
        for (int i = 1; i < n; i++){
            vector<int> next_meeting = intervals[i];
            
            if (current_meeting[1] > next_meeting[0]){
                return false;
            }
            
            current_meeting = next_meeting;
        }
        
        
        return true;
    }
};
