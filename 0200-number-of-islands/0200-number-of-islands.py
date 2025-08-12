class Solution:
    def dfs(self, grid, i, j):
        if i >= len(grid) or i < 0 or j >= len(grid[0]) or j < 0:
            return
        if grid[i][j] == "1":
            grid[i][j] = "0"
            self.dfs(grid, i - 1, j)
            self.dfs(grid, i + 1, j)
            self.dfs(grid, i, j - 1)
            self.dfs(grid, i, j + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    num_islands += 1
                    self.dfs(grid, i, j)
        return num_islands 