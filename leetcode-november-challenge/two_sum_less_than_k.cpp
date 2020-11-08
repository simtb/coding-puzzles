class Solution {
public:
    int twoSumLessThanK(vector<int>& A, int K) {
        int n = A.size();
        sort(A.begin(), A.end());
        
        int left = 0;
        int right = n - 1;
        int max_sum = INT_MIN;
        
        while (left < right){
            int current = A[left] + A[right];
            
            if (current < K){
                max_sum = max(max_sum, current);
                left++;
            }
            
            else{
                right--;
            }
        }
        
        if (max_sum == INT_MIN){
            return -1;
        }
        return max_sum;
    }
};
