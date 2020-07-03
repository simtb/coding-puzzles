"""
There are 8 prison cells in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.)

We describe the current state of the prison in the following way: cells[i] == 1 if the i-th cell is occupied, else cells[i] == 0.

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
"""

class Solution:
    def transform(self, cells: List[int]) -> List[int]:
        tmp: List[int] = [0] * 8
            
        for i in range(1, 7):
            tmp[i] = int(cells[i - 1] == cells[i + 1])
        
        return tmp
    
    
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        found: dict = {}
        for i in range(N):
            cells_str: str = str(cells)
            if cells_str in found:
                loop_length: int = i - found[cells_str]
                return self.prisonAfterNDays(cells, (N - i) % loop_length)
            else:
                found[cells_str] = i
                
        return cells
        
