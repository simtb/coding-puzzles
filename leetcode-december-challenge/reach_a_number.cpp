class Solution {
public:
    int reachNumber(int target) {
        int abs_target = abs(target);
        int current_total = 0;
        int i = 0;
        
        while (true){
            current_total += i;
            if (abs_target <= current_total){
                break;
            }
            
            i++;
        }
        
        if ((current_total - abs_target) % 2 == 0){
            return i;
        }
        
        else if ((current_total + (i + 1) - abs_target) % 2 == 0){
            return i + 1;
        }
        
        else{
            return i + 2;
        }
    }
};