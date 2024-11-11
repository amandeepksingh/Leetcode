class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    #     class Solution:
    # def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island_ct = 0
        nrows = len(grid)
        ncols = len(grid[0])

        def dfs (r, c):
            if r < nrows and r >= 0 and c < ncols and c >= 0 and grid[r][c] == "1":
                grid[r][c] = "0"
                # print(grid)
                dfs(r+1, c)
                dfs(r, c+1)
                dfs(r-1, c)
                dfs(r, c-1)
            return

        for r in range(nrows):
            for c in range(ncols):
                if grid[r][c] == "1":
                    island_ct += 1
                    dfs(r,c)
                
        return island_ct

 

            






