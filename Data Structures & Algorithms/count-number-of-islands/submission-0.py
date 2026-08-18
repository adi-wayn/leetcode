class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    self.dfs(grid, (r, c))
                    res += 1
        
        return res

    def dfs(self, grid: List[List[str]], node: tuple):
        if grid[node[0]][node[1]] == "1":
            grid[node[0]][node[1]] = "0"

        neighbors = [(node[0] + 1, node[1]), (node[0], node[1] + 1),
                    (node[0] - 1, node[1]), (node[0], node[1] - 1)]

        for neighbor in neighbors:
            if ((0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0])) and
            grid[neighbor[0]][neighbor[1]] == "1"):
                self.dfs(grid, neighbor)
