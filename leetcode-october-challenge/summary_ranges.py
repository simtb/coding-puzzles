"""
You are given a sorted unique integer array nums.

Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b
"""

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        summary_ranges: List[str] = []
        n: int = len(nums)
        
        if n == 0:
            return summary_ranges
        
        if n == 1:
            return [str(nums[0])]
        
        start: int = nums[0]
        current: int = nums[0]
        
        for i in range(1, n):
            tmp: int = nums[i]
            
            if tmp == current + 1:
                current += 1
            else:
                if start == current:
                    summary_ranges.append(str(start))
                else:
                    s: str = '{}->{}'.format(start, current)
                    summary_ranges.append(s)
                start = nums[i]
                current = nums[i]
        
        if start == current:
            summary_ranges.append(str(start))
        else:
            s: str = '{}->{}'.format(start, current)
            summary_ranges.append(s)
            
        return summary_ranges
