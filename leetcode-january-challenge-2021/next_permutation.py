class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        digits: List[int] = []
        
        for num in nums:
            digits.append(num)
        
        digits.sort()
        
        check: List[int] = digits[::-1]
        
        if (check == nums):
            nums.sort()
            return nums
        
        n: int = len(nums)
        right: int = n - 1
        
        for i in range(1, n):
            current_num: int = nums[n - i - 1]
            potentials: int = nums[n - i:]
            potentials.sort()
            m: int = len(potentials)
            for j in range(m):
                potential = potentials[j]
                if potential > current_num:
                    nums[n - i - 1] = potential
                    del potentials[j]
                    potentials.append(current_num)
                    potentials.sort()
                    
                    for k in range(m):
                        nums[n - i + k] = potentials[k]
                    return nums
        