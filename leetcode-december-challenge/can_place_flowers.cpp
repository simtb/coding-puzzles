class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        if (n == 0){
            return true;
        }
        
        int m = flowerbed.size();
        
        if (m == 1){
            if (flowerbed[0] == 1 && n > 0){
                return false;
            }
            
            if (flowerbed[0] == 0 && n > 1){
                return false;
            }
            
            return true;
        }
        
        for (int i = 0; i < m; i++){
            if (i == 0){
                if (flowerbed[i] == 0 && flowerbed[i + 1] == 0){
                    flowerbed[i] = 1;
                    n--;
                }
            }
            
            else if (i == m - 1){
                if (flowerbed[i - 1] == 0 && flowerbed[i] == 0){
                    flowerbed[i] = 1;
                    n--;
                }
            }
            
            else{
                if (flowerbed[i - 1] == 0 && flowerbed[i] == 0 && flowerbed[i + 1] == 0){
                    flowerbed[i] = 1;
                    n--;
                }
            }
            
            if (n == 0){
                break;
            }
        }
        
        return n == 0;
    }
};
