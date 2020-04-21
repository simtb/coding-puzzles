"""
A binary matrix means that all elements are 0 or 1. For each individual row of the matrix, this row is sorted in non-decreasing order.

Given a row-sorted binary matrix binaryMatrix, return leftmost column index(0-indexed) with at least a 1 in it. If such index doesn't exist, return -1.

You can't access the Binary Matrix directly.  You may only access the matrix using a BinaryMatrix interface:

BinaryMatrix.get(x, y) returns the element of the matrix at index (x, y) (0-indexed).
BinaryMatrix.dimensions() returns a list of 2 elements [n, m], which means the matrix is n * m.
Submissions making more than 1000 calls to BinaryMatrix.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

For custom testing purposes you're given the binary matrix mat as input in the following four examples. You will not have access the binary matrix directly.
"""

#solution 1 uses binary search (mlog(n)) where m is the number of rows and n is the number of columns
# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, x: int, y: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def _binarySearch(self, binaryMatrix: 'BinaryMatrix', y: int) -> int:
        left: int = 0
        right: int = binaryMatrix.dimensions()[1] - 1
        smallest_index: int = None
        
        while left <= right:
            mid: int = left + ((right - left) // 2)
        
            if binaryMatrix.get(y, mid) == 1:
                smallest_index: int = mid
                right: int = mid - 1
            else:
                left: int = mid + 1
        
        if smallest_index is not None:
            return smallest_index
        return None
        
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        if not binaryMatrix.dimensions()[0] or  not binaryMatrix.dimensions()[1]:
            return -1
        
        first_column: int = 100
            
        for i in range(binaryMatrix.dimensions()[0]):
            current_column: int = self._binarySearch(binaryMatrix, i)
            if current_column is not None:
                if current_column == 0:
                    return current_column
                else:
                    first_column: int = min(first_column, current_column)
        
        if first_column == 100:
            return -1
        else:
            return first_column





#solution 2 more efficient uses pointers

class Solution:
    def validPosition(self, binaryMatrix: 'BinaryMatrix', y: int, x: int) -> bool:
        if 0 <= y < binaryMatrix.dimensions()[0] and 0 <= x < binaryMatrix.dimensions()[1]:
            return True
        return False
    
    
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        if not binaryMatrix.dimensions()[0] or  not binaryMatrix.dimensions()[1]:
            return -1
        
        leftmost: int = 100
        y: int = 0
        x: int = binaryMatrix.dimensions()[1] - 1
        
        while True:
            if leftmost == 0:
                return leftmost
            if not self.validPosition(binaryMatrix, y, x):
                break
            
            value: int = binaryMatrix.get(y, x)
            print(value)
            if value == 1:
                leftmost: int = min(leftmost, x)
                x: int = x - 1
            else:
                y: int = y + 1
        
        if leftmost == 100:
            return -1
        return leftmost
            
