class Solution {
public:
    int kthFactor(int n, int k) {
        int a = 0;
        
        for (int i = 1; i < n + 1; i++){
            if (n % i == 0){
                a++;
                if (a == k){
                    return i;
                }
            }
        }
        
        return -1;
    }
};
