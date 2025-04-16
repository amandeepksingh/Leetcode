class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        c = 0 
        for i in range(len(grid)):
            row = grid[i]
            for j in range(len(grid[0])): # n x n so can also just be len(grid)
                col = [row[j] for row in grid]
                if col == row:
                    c = c + 1
        return c 